if pushd /var/www/html/primer-server; then
    echo "/var/www/html/primer-server exists"
    popd
else
	echo "/var/www/html/primer-server doesn't exist"
	echo "making /var/www/html/primer-server"
	mkdir /var/www/html/primer-server
fi

echo "copying ui/v$1 to /var/www/html/primer-server/v$1"
rm -R /var/www/html/primer-server/v$1
cp -R ui/v$1 /var/www/html/primer-server/v$1

echo "RewriteEngine on" > /var/www/html/.htaccess
echo "RewriteRule ^primer-server/?$ http://18.219.153.20/primer-server/v$1/ [R=302,L]" >> /var/www/html/.htaccess
