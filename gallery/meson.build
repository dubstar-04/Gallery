pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'gallery')
widgetsdir = join_paths(moduledir, 'widgets')

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'gallery.in',
  output: 'gallery',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)

gallery_sources = [
  '__init__.py',
  'main.py',
  'window.py',
  'library.py',
]

widget_sources = [
  'widgets/__init__.py',
  'widgets/image_widget.py',

]

install_data(gallery_sources, install_dir: moduledir)
install_data(widget_sources, install_dir: widgetsdir)
