# construction-evaluation_vuewithdjango

appfront目录下
npm install
npm run dev试运行看看依赖有没有报错

数据库的创建
create database btesdb;

BTESDB文件夹下的migrations文件夹下 把除了init外的所有文件删掉

manager.py同级目录下
python manage.py makemigrations
python manage.py migrate


最后
python manage.py runserver 0.0.0.0:8000

可能有的地方记错，哪一步出问题再补充
