from anexo2.docs import Anexo2


def test_base():

    hospital = {'nombre': 'HOSPITAL SAN ROQUE',  # https://www.sssalud.gob.ar/index.php?page=bus_hosp&cat=consultas
            'codigo_hpgd': '4321323'}
            
    beneficiario = {'apellido_y_nombres': 'Juan Perez',
                    'tipo_dni': 'DNI',  # | LE | LC
                    'dni': '34100900',
                    'tipo_beneficiario': 'titular',  # | no titular | adherente
                    'parentesco': 'conyuge',  # hijo | otro
                    'sexo': 'M',  # | F
                    'edad': 88}
    atencion = {'tipo': ['consulta', 'práctica', 'internación'],
                'especialidad': 'Va un texto al parecer largo, quizas sea del nomenclador',
                'profesional': {
                    'apellido_y_nombres': 'MARTÍNEZ, Adolfo',
                    'matricula_profesional': '10542',
                },
                'codigos_N_HPGD': ['AA01', 'AA02', 'AA06', 'AA07'],  # no se de donde son estos códigos
                'fecha': {'dia': 3, 'mes': 9, 'anio': 2019},
                'diagnostico_ingreso_cie10': {'principal': 'W020', 'otros': ['w021', 'A189']}}
    obra_social = {'codigo_rnos': '800501',
                'nombre': 'OBRA SOCIAL ACEROS PARANA',
                'nro_carnet_obra_social': '9134818283929101',
                'fecha_de_emision': {'dia': 11, 'mes': 9, 'anio': 2009},
                'fecha_de_vencimiento': {'dia': 11, 'mes': 9, 'anio': 2029}}
    empresa = {'nombre': 'Telescopios Hubble',
            'direccion': 'Av Astronómica s/n',
            'ultimo_recibo_de_sueldo': {'mes': 7, 'anio': 2019},
            'cuit': '31-91203043-8'}

    data = {'dia': 3,
            'mes': 9,
            'anio': 2019,
            'hospital': hospital,
            'beneficiario': beneficiario,
            'atencion': atencion,
            'obra_social': obra_social,
            'empresa': empresa
            }

    anx = Anexo2(data=data)
    res = anx.get_html()
    assert res is not None