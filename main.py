import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.utils import platform

if platform == 'android':
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])

class CleanerApp(App):
    def build(self):
        self.title = "Poco X3 Cleaner"
        layout = BoxLayout(orientation='vertical', padding=40, spacing=30)
        
        self.header_label = Label(
            text="🧹 POCO X3 SUPER CLEANER",
            font_size=22,
            size_hint=(1, 0.2),
            color=(0.1, 0.8, 0.9, 1)
        )
        layout.add_widget(self.header_label)
        
        self.status_label = Label(
            text="Nhấn nút bên dưới để bắt đầu quét rác hệ thống...",
            font_size=16,
            size_hint=(1, 0.5),
            halign='center',
            valign='middle',
            color=(1, 1, 1, 1)
        )
        self.status_label.bind(size=self.status_label.setter('text_size'))
        layout.add_widget(self.status_label)
        
        self.clean_btn = Button(
            text="DỌN DẸP NGAY",
            font_size=18,
            size_hint=(1, 0.3),
            background_color=(0.1, 0.6, 0.8, 1)
        )
        self.clean_btn.bind(on_press=self.start_cleaning)
        layout.add_widget(self.clean_btn)
        
        return layout

    def start_cleaning(self, instance):
        self.status_label.text = "🔄 Đang quét bộ nhớ và file rác..."
        
        target_dirs = [
            "/sdcard/Download/Temp",
            "/sdcard/MIUI/debug_log",
            "/sdcard/Android/data/com.tencent.ig/cache",
            "/sdcard/Android/data/com.pubg.krmobile/cache",
            "/sdcard/WhatsApp/Media/WhatsApp Video/Sent",
            "/sdcard/Telegram/Telegram Video"
        ]
        
        total_freed = 0
        files_deleted = 0
        
        for folder in target_dirs:
            if os.path.exists(folder):
                for root, dirs, files in os.walk(folder):
                    for file in files:
                        file_path = os.path.join(root, file)
                        try:
                            file_size = os.path.getsize(file_path)
                            os.remove(file_path)
                            total_freed += file_size
                            files_deleted += 1
                        except Exception:
                            pass
                            
        mb_freed = total_freed / (1024 * 1024)
        self.status_label.text = f"✨ DỌN DẸP HOÀN TẤT!

- Đã xóa: {files_deleted} file rác
- Giải phóng: {mb_freed:.2f} MB"

if __name__ == "__main__":
    CleanerApp().run()
