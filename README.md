# ET-SL Website Projekt

Dieses Projekt enthält die Website für die ET-SL GmbH (Elektrotechnik Schöcklland).

## Projektstruktur

- `/` (Root): Enthält alle öffentlich zugänglichen HTML-Seiten (`index.html`, `photovoltaik.html`, etc.) sowie Konfigurationsdateien wie `robots.txt` und `sitemap.xml`.
- `assets/`: 
  - `css/`: Stylesheets (Hauptdatei: `main.css`).
  - `fonts/`: Lokal eingebundene Schriften (DSGVO-konform).
  - `img/`: Aktive Bilder für die Website.
  - `js/`: JavaScript-Dateien.
  - `vendor/`: Drittanbieter-Bibliotheken (AOS, GLightbox, Bootstrap Icons).
- `tools/`: Hilfsskripte zur Wartung der Website.
- `archive/`: Sicherungskopien alter Logos, Quelldaten und Originalbilder, die nicht direkt auf der Website verwendet werden.

## Wartung

### Seiten generieren
Im Verzeichnis `tools/` befindet sich ein Skript `generate_pages.py`. 
**ACHTUNG:** Dieses Skript ist momentan veraltet und enthält nicht die neuesten SEO- und Barrierefreiheits-Optimierungen. Vor einer erneuten Verwendung müssen die Templates im Skript aktualisiert werden.

### SEO & Barrierefreiheit
Die Website ist für SEO (JSON-LD, Breadcrumbs) und Barrierefreiheit (Skip-Links, semantisches HTML) optimiert. Bei Änderungen an den HTML-Dateien sollte auf den Erhalt dieser Strukturen geachtet werden.
