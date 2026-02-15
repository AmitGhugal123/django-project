## ▶️ Run Project (Every Time You Open)

### 🖥️Terminal 2 → Django
```bash
.venv\Scripts\activate
cd newone
python manage.py runserver
```

### 🖥️ Terminal 1 — Tailwind

```bash
.venv\Scripts\activate
cd newone
python manage.py tailwind start
```

### path for all_student
http://127.0.0.1:8000/firstone/

### path for admin
http://127.0.0.1:8000/admin/


### after updating models
python manage.py makemigrations firstone
python manage.py migrate






all....html
{% comment %} {% extends "layout.html" %}

{% block title %}
Home
{% endblock %}

{% block content %}

<h1 style="text-align:center; margin-top:20px;">All Students</h1>

<div style="
    display:grid;
    grid-template-columns:repeat(auto-fit, minmax(250px,1fr));
    gap:20px;
    padding:30px;
">

{% for student in students %}
    <div style="
        background:#ffffff;
        padding:20px;
        border-radius:12px;
        box-shadow:0 4px 12px rgba(0,0,0,0.1);
        text-align:center;
        transition:0.3s;
    "
    onmouseover="this.style.transform='scale(1.03)'"
    onmouseout="this.style.transform='scale(1)'"
    >

        {% if student.profile_pic %}
            <img src="{{ student.profile_pic.url }}" 
                 style="
                 width:100%;
                 height:180px;
                 object-fit:cover;
                 border-radius:10px;
                 margin-bottom:10px;
                 ">
        {% else %}
            <div style="
                width:100%;
                height:180px;
                background:#eee;
                border-radius:10px;
                margin-bottom:10px;
                display:flex;
                align-items:center;
                justify-content:center;
            ">
                No Image
            </div>
        {% endif %}

        <h2 style="margin:10px 0;">{{ student.name }}</h2>

        <p style="color:gray;">Age: {{ student.age }}</p>
        <p style="color:gray;">Course: {{ student.course }}</p>

        <button style="
            margin-top:10px;
            padding:8px 15px;
            border:none;
            background:#ff6b00;
            color:white;
            border-radius:6px;
            cursor:pointer;
        ">
            View Profile
        </button>

    </div>

{% empty %}
    <p style="text-align:center;">No students found</p>
{% endfor %}

</div>

{% endblock %} {% endcomment %}