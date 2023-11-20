# dstoolbox-2-66-64114540498
private project for ds toolbox class.
07/11/2566

    ติดตั้ง scoop.sh

    ติดตั้ง github-cli

      scoop install git
      #scoop bucket add main
      scoop install gh

    สร้างสภาพแวดล้อมใหม่

      python -m venv venv
      venv\Scripts\activate

    ติดตั้ง package

      pip install django

14/11/2566

    สร้าง github repository ของตัวเอง

      Username/dstoolbox-2-66-66xxxxxxxx

    เพิ่ม wichit2s เป็น collaborator

    การเข้าใช้งาน github

      gh auth login
      gh repo clone Username/dstoolbox-2-66-66xxxxxxxx

    เริ่มเขียน markdown

    การเขียนเอกสารบน Github

    github.com/cookiecutter/cookiecutter-django

    venv\Scripts\activate pip install django pre-commit pip install cookiecutter cookiecutter gh:cookiecutter/cookiecutter-django
