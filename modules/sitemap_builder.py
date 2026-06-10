import os
from datetime import datetime

def generar_sitemap(paginas, base_dir):
    fecha = datetime.now().strftime("%Y-%m-%d")
    base_url = "https://tudominio.com"
    
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    for ruta in paginas[:500]:
        rel = ruta.replace(base_dir, "").lstrip("/")
        sitemap += f'  <url><loc>{base_url}/{rel}</loc><lastmod>{fecha}</lastmod><priority>0.9</priority></url>\n'
    
    sitemap += '</urlset>'
    
    with open(os.path.join(base_dir, 'sitemap.xml'), 'w', encoding='utf-8') as f:
        f.write(sitemap)

def generar_robots_txt(base_dir):
    robots = 'User-agent: *\nAllow: /\nSitemap: https://tudominio.com/sitemap.xml\n'
    with open(os.path.join(base_dir, 'robots.txt'), 'w', encoding='utf-8') as f:
        f.write(robots)
