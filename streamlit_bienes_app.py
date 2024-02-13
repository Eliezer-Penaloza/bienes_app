import streamlit as st
import pandas as pd

#def local_css(file_name):
#    with open(file_name) as f:
#        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

#local_css("style.css")

l = ['Fecha', 'Dependencia', 'Unidad', 'Ubicación', 'Estado', 'Región',
       'Cedula_Resp_Uso', 'Responsable_Uso', 'Cedula_Resp_Indiv',
       'Responsable_Individual', 'ID_Unidad', 'Grupo', 'Sub_Grupo', 'Nro_Bien',
       'Tipo', 'Caracteristicas', 'Marca', 'Modelo', 'Serial', 'Estatus',
       'Stock', 'Observaciones', 'Contador', 'Proveedor', 'Cedula_RIF',
       'Nro_O_Compra', 'Nro_SEP', 'Nro_Factura', 'Fecha_Factura',
       'Precio_Uni_Bs', 'IVA', 'Total_Bs', 'Tasa_BCV', 'Total_$',
       'Inv_Inicial', 'Entradas', 'Salidas', 'Inv_Final']

lista_dependencias = ['','Dirección General Territorial',
 'Oficina de Seguimiento y Evaluación de Políticas Públicas',
 'Oficina de Tecnología de la Información y la Comunicación',
 'Oficina de Gestión Administrativa',
 'Dirección de Línea de Bienes Nacionales y Servicios',
 'Dirección General del Despacho',
 'Oficina de Consultoría Juridíca',
 'Oficina de Planificación y Presupuesto',
 'Dirección General de Gestión Estratégica',
 'Oficina de Gestión Administrativa ',
 'Dirección General de Operaciones',
 'Oficina de Auditoria Interna',
 'Dirección General de Finanzas',
 'Oficina de Gestión Humana',
 'Oficina de Atención al Ciudadano',
 'Oficina de Gestión Comunicacional',
 'Dirección General Técnica de Proyectos',
 'Dirección Ejecutiva']

lista_unidades = ['','URE Zulia',
 'URE Yaracuy',
 'URE Nueva Esparta',
 'URE La Guaira',
 'Oficina de Seguimiento y Evaluación de Políticas Públicas',
 'Oficina de Tecnología de la Información y la Comunicación',
 'Oficina de Gestión Administrativa',
 'Depósito',
 'Cocina',
 'Dirección General del Despacho',
 'Unidad de Transporte',
 'Dirección de Línea de Bienes Nacionales y Servicios',
 'URE Bolívar',
 'Oficina de Consultoría Juridíca',
 'Archivo',
 'Dirección de Línea de Planificación y Organización',
 'URE Barinas',
 'Dirección General de Gestión Estratégica',
 'URE Apure',
 'URE Guarico',
 'URE Táchira',
 'URE Mérida',
 'URE Trujillo',
 'URE Monagas',
 'URE Delta Amacuro',
 'Dirección de Línea de Prevención',
 'Dirección General de Operaciones',
 'Oficina de Auditoria Interna',
 'Dirección General de Finanzas',
 'URE Portuguesa',
 'Dirección de Línea de Análisis de Inversiones',
 'Dirección General de Gestión Humana',
 'Cuarto de Impresión',
 'Servicio de Atención Primaria',
 'Oficina de Atención al Ciudadano',
 'Oficina de Gestión Comunicacional',
 'URE Miranda y Distrito Capital',
 'Dirección General Territorial',
 'Dirección General Técnica de Proyectos',
 'Dirección de Línea de Asistencia Técnica Integral ',
 'Dirección Ejecutiva',
 'Sala de Maquinas',
 'Sala de Reuniones Pequeña',
 'Sala de Reuniones Santa Ines',
 'Sala de Reuniones Ezequiel Zamora',
 'Recepción Interna',
 'Recepción Externa',
 'Cuarto de Conductores',
 'Comedor',
 'Sala de Reuniones Batalla de Corozo',
 'Sala de Carga',
 'Dirección de Línea de Planificación y Presupuesto',
 'Dirección de Línea de Administración',
 'URE Anzoategui',
 'URE Aragua',
 'URE Falcón',
 'URE Amazonas',
 'URE Cojedes',
 'URE Lara',
 'URE Sucre',
 'URE Carabobo']

lista_unidades.sort()

lista_estados = ['','Zulia',
 'Yaracuy',
 'Nueva Esparta',
 'La Guaira',
 'Distrito Capital',
 'Bolívar',
 'Barinas',
 'Apure',
 'Guárico',
 'Táchira',
 'Mérida',
 'Trujillo',
 'Monagas',
 'Delta Amacuro',
 'Portuguesa',
 'Anzoategui',
 'Aragua',
 'Falcón',
 'Amazonas',
 'Cojedes',
 'Lara',
 'Sucre',
 'Carabobo']

lista_estados.sort()

lista_dependencias.sort()

lista_region = ['','Región Occidente',
 'Región Centro Occidente',
 'Región Insular',
 'Región Capital',
 'Región Guayana',
 'Región Los LLanos',
 'Región Los Andes',
 'Región Oriente',
 'Región Centro']

lista_region.sort()

st.set_page_config(layout="wide")



with st.form('Form 1', clear_on_submit= True):


    fecha_control = pd.Timestamp.today() 
    print(fecha_control)

    col1, col2, col3 = st.columns(3)

    fecha = col1.date_input('Fecha:')
    print('Fecha',fecha)

    dependencias = col2.selectbox('Dependencia:', options= lista_dependencias)
    if dependencias == '':
        st.warning('Por favor, elija una Dependencia.')

    unidad = col3.selectbox('Unidad', options = lista_unidades)
    if unidad == '':
        st.warning('Por favor, elija una Unidad.')

    ubicacion = col1.text_input('Ubicación:')
    if ubicacion == '':
        st.warning('Por favor, elija una Ubicación.')

    estado = col2.selectbox('Estado:', options= lista_estados)
    if estado == '':
        st.warning('Por favor, elija un Estado.')


    region = col3.selectbox('Región:', options=lista_region)
    if region == '':
        st.warning('Por favor, elija una Región.')

    cedula_resp_uso = col1.text_input('Cédula responsable de uso:')  
    responsable_uso = col2.text_input('Nombre y apellido del responsable:')
    responsable_individual = col3.text_input('Responsable individual')
    id_unidad = col1.text_input('ID Unidad:')
    grupo = col2.text_input('Grupo:')
    subgrupo = col3.text_input('Sub Grupo:')
    nro_bien = col1.text_input('Número bien:')
    tipo = col2.text_input('Tipo:')
    caracteristicas = col3.text_input('Caractéristicas:')
    marca = col1.text_input('Marca:')
    modelo = col2.text_input('Modelo:')
    serial = col3.text_input('Serial:')
    estatus = col1.text_input('Estatus:')
    stock = col2.text_input('Stock:')
    observaciones = col3.text_area('Observaciones:')





    st_state = col2.form_submit_button('Guardar')

    
