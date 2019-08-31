import os
from jinja2 import Template


class Anexo2:
    """ Generacion del Anexo II """

    here = os.path.dirname(os.path.realpath(__file__))
    templates_folder = os.path.join(here, 'templates')
    default_template = os.path.join(templates_folder, 'Anexo-II-RESOLUCION-487-2002.html')

    def validate_data(self, data):
        # validate and add missing info
        # from sisa we can get person info
        # from oss_ar we can get OSS info

        # HPGD = Hospitales Públicos de Gestión Descentralizada

        return data

    def get_html(self, data, template_path=None, save_path=None):
        if template_path is None:
            template_path = self.default_template

        validated_data = self.validate_data(data=data)
        f = open(template_path)
        template = Template(f.read())
        html = template.render(**validated_data)
        if save_path is not None:
            f = open(save_path, 'w')
            f.write(html)
            f.close()

        return html


if __name__ == '__main__':
    a2 = Anexo2()
    save_to = os.path.join(a2.templates_folder, 'res.html')

    data = {'dia': '03',
            'mes': '09',
            'anio': '2019',
            'hospital': {
                'nombre': 'HOSPITAL SAN ROQUE',  # https://www.sssalud.gob.ar/index.php?page=bus_hosp&cat=consultas
                'codigo_hpgd': '4321323'
                },
            'beneficiario': {
                'apellido_y_nombres': 'Juan Perez',
                'tipo_dni': 'DNI',  # | LE | LC
                'dni': '34100900',
                'tipo_beneficiario': 'titular',  # | no titular | adherente
                'parentesco': 'conyuge',  # hijo | otro
                'sexo': 'm',  # | f
                'edad': 88,
                },
            'atencion': {
                'tipo': 'consulta',  # | practica | internacion
                'especialidad': 'Va un texto al parecer largo, quizas sea del nomenclador',
                'codigos_N_HPGD': ['AA01', 'AA02', 'AA06', 'AA07'],  # no se de donde son estos códigos
                'fecha': {'dia': '03', 'mes': '09', 'anio': '2019'},
                'diagnostico_ingreso_cie10': {'principal': 'W020', 'otros': ['w021', 'A189']}
                },
            'obra_social': {
                'codigo_rnos': '800501',
                'nombre': 'OBRA SOCIAL ACEROS PARANA',
                'nro_carnet_obra_social': '9134818283929101',
                'fecha_de_emision': {'dia': '11', 'mes': '09', 'anio': '2009'},
                'fecha_de_vencimiento': {'dia': '11', 'mes': '09', 'anio': '2029'}
                },
            'empresa': {
                'nombre': 'Telescopios Hubble',
                'direccion': 'Av Astronómica s/n',
                'ultimo_recibo_de_sueldo': {'mes': '07', 'anio': '2019'},
                'cuit': '31-91203043-8'
                }
        }

    a2.get_html(data=data, save_path=save_to)