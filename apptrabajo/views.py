from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def personal(request):
    data={
    'titulo1':'Sección de Personal',
    'personal':[
    {
        'nombre':'Josué Varela',
        'cargo':'Director de Reclutamiento',
        'descripcion':'Josué cuenta con más de 10 años de experiencia en la industria de recursos humanos y tecnología. Lidera el equipo de reclutamiento, diseñando estrategias para conectar a las empresas con el mejor talento. Es experto en procesos de selección para startups y empresas tecnológicas de rápido crecimiento. Josué también se especializa en la creación de programas de desarrollo de talento interno. Su enfoque está en el liderazgo inclusivo y la diversidad en los equipos de trabajo. Su cantidad de años de experiencia reflejan el gran trabajo que realiza día a día en nuestra empresa..',
        'imagenes': [
            'images/josue.jpeg'
        ],
        'imagenes2': [
            'images/10.PNG'
        ]
    },
    {
        'nombre':'Santiago Pérez',
        'cargo':'Especialista en Reclutamiento IT',
        'descripcion':'Santiago es ingeniero en informática con 8 años de experiencia en la selección de perfiles tecnológicos. Su carrera en TechTalent Connect se ha centrado en encontrar desarrolladores, ingenieros de software y especialistas en ciberseguridad para empresas internacionales. Santiago tiene un enfoque proactivo y personalizado para cada cliente, adaptándose a las necesidades específicas de cada proyecto. Es conocido por su habilidad para descubrir talento en sectores emergentes como la inteligencia artificial y el blockchain.',
        'imagenes': [
            'images/santi.jpeg'
        ],
        'imagenes2': [
            'images/8.PNG'
        ]
    },
    {
        'nombre':'Ana Torres',
        'cargo':'Coordinadora de Desarrollo Profesional',
        'descripcion':'Con un background en psicología organizacional, Ana ha trabajado en el desarrollo y la capacitación de talento por más de 7 años. En TechTalent Connect, lidera programas de formación y mentoring para los egresados que buscan ingresar al mercado laboral tecnológico. Su pasión es ayudar a los jóvenes profesionales a desarrollar sus habilidades técnicas y blandas. Ana es una firme defensora del crecimiento profesional continuo y colabora estrechamente con empresas para entender las tendencias y demandas del sector IT.',
        'imagenes': [
            'images/ana.jpeg',
        ],
        'imagenes2': [
            'images/7.PNG'
        ]
    }
    ]}
    return render(request, 'info.html',data)

def clientes(request):
    data={
    'titulo2':'Sección de Clientes',
    'clientes':[
    {
        'nombre':'Martín Suárez',
        'profesion':'CTO en InnovApp',
        'reseña':'Gracias a TechTalent Connect, hemos logrado contratar a desarrolladores de software de alta calidad en tiempo récord. Su enfoque personalizado ha sido clave para nuestro crecimiento.',
        'imagenes': [
            'images/martin.jpeg'
        ],
        'imagenes2': [
            'images/star.PNG'
        ]
    },
    {
        'nombre':'Laura Méndez',
        'profesion':'Gerente de Recursos Humanos en GlobalTech Solutions',
        'reseña':'La rapidez y precisión de TechTalent Connect para encontrar perfiles IT especializados ha sido fundamental para cubrir nuestras necesidades de personal.',
        'imagenes': [
            'images/laura.jpeg'
        ],
        'imagenes2': [
            'images/star.PNG'
        ]
    },
    {
        'nombre':'Roberto Silva',
        'profesion':'Fundador de DataNova',
        'reseña':'TechTalent Connect ha sido nuestro socio estratégico en la contratación de expertos en análisis de datos. Su capacidad para identificar talento ha marcado la diferencia.',
        'imagenes': [
            'images/roberto.jpeg'
        ],
        'imagenes2': [
            'images/star.PNG'
        ]
    }
    ]}
    return render(request, 'info.html',data)


def egresados(request):
    data={
    'titulo3':'Sección de Egresados',
    'egresados':[
    {
        'nombre':'Camila Rojas',
        'empresa':'SoftDev Corp',
        'opinion':'TechTalent Connect fue el puente perfecto para encontrar mi primer empleo en desarrollo web. Su apoyo en todo el proceso fue clave para lograrlo, y estoy agradecida por la orientación recibida.',
        'imagenes': [
            'images/camila.jpeg'
        ],
        'imagenes2': [
            'images/egresado2023.PNG'
        ]
    },
    {
        'nombre':'Javier Morales',
        'empresa':'CloudNet Technologies',
        'opinion':'La capacitación ofrecida por TechTalent Connect me preparó para enfrentar los retos del mundo IT. Hoy trabajo como ingeniero de redes y la experiencia fue excelente.',
        'imagenes': [
            'images/javier.jpeg'
        ],
        'imagenes2': [
            'images/egresado2020.PNG'
        ]
    },
    {
        'nombre':'Paula Fernández',
        'empresa':'InnovCode Labs',
        'opinion':'Gracias a TechTalent Connect conseguí mi puesto como analista de datos. Su programa me ayudó a desarrollar las habilidades que necesitaba para destacarme en el sector tecnológico.',
        'imagenes': [
            'images/paula.jpeg'
        ],
        'imagenes2': [
            'images/egresado2014.PNG'
        ]
    }
    ]}
    return render(request, 'info.html',data)