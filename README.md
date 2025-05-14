# Hospital-Management-Software

Funcionalidades implementadas:

 • Patient Registration: Patients can register and maintain their profiles;
 • Appointment Scheduling: Patients can book, cancel, and reschedule appointments with doctors;
 • Medical Record Management: Secure storage and access to patient medical records;
 • Billing and Invoicing: Automated billing for medical services rendered;
 • Prescription Management: Doctors can create and manage prescriptions;
 • Lab Test Ordering and Reporting: Ordering lab tests and accessing results;
 • Ward and Bed Management: Management of hospital wards and bed allocations;
 • Inventory Management: Management of medical supplies and inventory;
 • Staff Scheduling: Scheduling shifts and duties for hospital staff;
 • Emergency Services Management: Handling and prioritizing emergency cases.

Padrões de Projeto utilizados:

 • Factory Method (criacional): em hospital.py, o Factory Method é usado para "fabricar" novos funcionários, diferenciando-os-os em seus subgrupos (médicos, enfermeiros ou outros cargos)
 • Singleton (criacional): utilizado em hospital.py para garantir que hospital será instanciado uma única vez, que apesar de ocorrer uma vez no código atual (em main.py), em uma possível alteração futura do código que venha instanciar em outro lugar do código não cause problemas
 • Decorator (estrutural): utilizado em patients.py para diminuir o número de chamadas de função relacionadas a printar informações do paciente. O que deve ser printado fica guardado em um objeto printer, do tipo InfoPrinter, que vai ser decorado com outras subclasses relacionadas ao que pode ser printado (registros médicos, prescrições, etc.)
 • Observer (comportamental): utilizado em patients.py para notificar o médico sobre qualquer coisa relevante que for adicionada ao perfil do paciente
