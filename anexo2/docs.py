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

    data ={'dia': '03',
           'mes': '09',
           'anio': '2019'
            }

    a2.get_html(data=data, save_path=save_to)