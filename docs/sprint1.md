# Sprint 0: Concepción y Arquitectura SaaS 🏗️

**Objetivo:** Establecer la infraestructura técnica y el diseño de la plataforma multi-sistema "Willy Systems".

### Tareas:
- [x] Definición de la arquitectura SaaS para albergar múltiples proyectos.
- [x] Configuración de la Landing Page principal (Portal Maestro) con diseño responsivo.
- [x] Estrategia de integración del Sistema de Ventas (Java) mediante redirección externa.
- [x] Selección del stack tecnológico: Flask para el backend y Tailwind CSS para el diseño móvil.
- [x] Vinculación del entorno de desarrollo con GitHub Codespaces para trabajo en la nube.

**Definición de Hecho (DoD):** El usuario debe poder acceder a una página de inicio profesional donde pueda elegir entre entrar a VCvet o redirigirse al Sistema de Ventas.
# Sprint 1: Estructura Base y Registro 🐾

**Objetivo:** Crear la interfaz de bienvenida y el formulario para capturar datos de mascotas.

### Tareas:
- [x] Configuración de entorno (Codespaces + Flask).
- [x] Arquitectura Modular con `base.html`.
- [x] Formulario de Registro de Pacientes.
- [x] Sistema de Notificaciones (Flash Messages).
- [x] Validación de registro de un paciente real.

**Definición de Hecho (DoD):** El usuario debe poder ver la web, llenar un formulario y ver un mensaje de "Registro Exitoso".

# Sprint 2: Persistencia de Datos y Gestión Operativa 💾

**Objetivo:** Implementar una base de datos para guardar la información de las mascotas y crear un panel para administrarlas.

### Tareas:
- [x] Configuración de la base de datos local (**SQLite**) para el almacenamiento permanente.
- [x] Creación del modelo de datos para la tabla "Pacientes" (Nombre, Especie, Dueño).
- [x] Integración de SQLAlchemy para conectar el formulario de registro con la base de datos.
- [x] Validación de registro exitoso con persistencia real (Caso Bella).
- [ ] Creación de una nueva vista de Dashboard para listar todos los pacientes registrados.
- [ ] Implementación de funciones básicas de gestión (Eliminar o Editar registros).
- [ ] Ajuste del Dashboard para visualización correcta en dispositivos móviles.

**Definición de Hecho (DoD):** Al registrar una mascota y reiniciar el sistema, los datos deben permanecer guardados y ser visibles en una tabla de administración.

# Sprint 3: Visualización y Filtros de Datos 🔍

**Objetivo:** Implementar la visualización masiva de registros y herramientas de búsqueda para facilitar la navegación del usuario.

### Tareas:
- [ ] Creación de la vista "Listado de Pacientes" con diseño de tabla responsiva.
- [ ] Implementación de lógica de consulta (Query) para traer todos los datos de SQLite.
- [ ] Desarrollo de un buscador por nombre de mascota o nombre del dueño.
- [ ] Añadir contadores automáticos en el Dashboard (Ej: "Total de Pacientes").
- [ ] Optimización de la interfaz para lectura cómoda en pantallas de celulares.
- [ ] Integración de iconos de estado para diferenciar especies (Caninos, Felinos, etc.).

**Definición de Hecho (DoD):** El usuario debe poder entrar a una nueva sección, ver la lista completa de mascotas registradas y encontrar una específica usando el buscador.