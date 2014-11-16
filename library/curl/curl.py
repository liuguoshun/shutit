"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class curl(ShutItModule):


	def is_installed(self, shutit):
		return False


	def build(self, shutit):
		shutit.send('mkdir -p /opt/curl')
		shutit.send('pushd /opt/curl')
		shutit.send('wget http://curl.haxx.se/download/curl-7.39.0.tar.gz')
		shutit.send('gunzip curl-7.39.0.tar.gz')
		shutit.send('tar -xf curl-7.39.0.tar')
		shutit.send('pushd curl-7.39.0')
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		shutit.send('popd')
		shutit.send('popd')
		shutit.send('rm -rf /opt/curl')
		return True

	#def get_config(self, shutit):
	#	return True

	#def check_ready(self, shutit):
	#	return True
	
	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#	return True

	#def finalize(self, shutit):
	#	return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return curl(
		'shutit.tk.curl.curl', 0.01251613624,
		description='',
		maintainer='',
		depends=['shutit.tk.make.make']
	)

