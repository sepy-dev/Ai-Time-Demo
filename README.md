# 🧠 AI Time Demo

This repository is a **demo version** of a smart scheduling system using **AI, NLP, and Django**.  
It is currently under development and intended to showcase basic integration between a frontend calendar and a backend powered by Django.

> ⚠️ This is not a production-ready project. It is shared for educational and prototype purposes.

---

## 📌 Project Goals

The aim of this demo is to experiment with:
- Natural Language Processing (NLP) to interpret task content and suggest appropriate time slots.
- A calendar UI (using Vue Cal) connected to a Django backend.
- Future integration of machine learning models to auto-schedule tasks intelligently.

---

## 🚀 Quick Start (Local Setup)

1. **Clone the repository**
   ```bash
   git clone https://github.com/sepy-dev/Ai-Time-Demo.git
   cd Ai-Time-Demo

    Create virtual environment & install dependencies

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Run Django server

    python manage.py migrate
    python manage.py runserver

    Frontend Setup (optional)
    If you want to test with the Vue Cal frontend, go to the frontend/ directory and follow its README instructions (to be added).

🎁 Purpose of Sharing

This repository is shared to help others understand:

    How to connect frontend calendar components with Django APIs

    How to use NLP to improve productivity tools

    How to structure such projects for future AI enhancement

Feel free to fork, play with it, or suggest improvements via pull requests.
📜 License

MIT License
🧠 دموی زمان‌بندی هوشمند

این مخزن نسخه‌ی دموی آزمایشی یک سیستم زمان‌بندی هوشمند بر پایه‌ی هوش مصنوعی، پردازش زبان طبیعی (NLP) و جنگو (Django) است.
هدف آن نمایش یکپارچه‌سازی اولیه بین تقویم فرانت‌اند و بک‌اند جنگو است.

    ⚠️ این پروژه آماده استفاده در محیط واقعی نیست و صرفاً برای اهداف آموزشی و آزمایش منتشر شده است.

📌 اهداف پروژه

این دمو برای آزمایش موارد زیر طراحی شده:

    تحلیل محتوای تسک‌ها با NLP برای پیشنهاد زمان مناسب

    اتصال تقویم (Vue Cal) به بک‌اند جنگو

    افزودن مدل‌های یادگیری ماشین برای زمان‌بندی هوشمند در آینده

🚀 راه‌اندازی سریع

    کلون کردن پروژه

git clone https://github.com/sepy-dev/Ai-Time-Demo.git
cd Ai-Time-Demo

ساخت محیط مجازی و نصب وابستگی‌ها

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

اجرای سرور جنگو

    python manage.py migrate
    python manage.py runserver

    نصب فرانت‌اند (اختیاری)
    اگر قصد تست Vue Cal را دارید، وارد پوشه frontend/ شوید و راهنمای آن را دنبال کنید (در آینده اضافه خواهد شد).

🎁 هدف از انتشار

هدف از اشتراک‌گذاری این پروژه:

    آموزش اتصال تقویم‌های تعاملی به بک‌اند جنگو

    بررسی استفاده از NLP در ابزارهای بهره‌وری

    کمک به توسعه پروژه‌های مشابه با تمرکز بر هوش مصنوعی

اگر دوست دارید، این ریپو را فورک کنید، با آن کار کنید یا بهبودهای پیشنهادی را با Pull Request ارسال کنید.
