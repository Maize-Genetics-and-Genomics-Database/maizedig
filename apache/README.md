
#### Structure of Directories & Files
```
apache/
└── django.wsgi
```  

#### WSGI set up

It should be added `WSGIScriptAlias` into the apache configuration (/etc/httpd/conf/httpd.conf). 
We use virtual host for MaizeDIG web service and 
`WSGIScriptAlias` can be added under `<VirtualHost>`. 

    WSGIScriptAlias / "/var/www/MaizeDIG/apache/django.wsgi"
        
Please see the sample configuration belows:

    [File] /etc/httpd/conf/httpd.conf
    ...
    ##################################################################
    #
    # Virtual Host Settings
    #
    
    #
    # MaizeDIG
    #
    <VirtualHost maizedig.usda.iastate.edu:80>
        ServerName maizedig.maizegdb.org
        DocumentRoot /var/www/MaizeDIG
        ServerAlias maizedig.maizegdb.org
        ServerAdmin totaks@gmail.com
            
        WSGIDaemonProcess maizedig.maizegdb.org user=mdig group=mdig processes=2 threads=25 python-path=/var/www/MaizeDIG:/usr/lib/python2.7/site-packages
        WSGIProcessGroup maizedig.maizegdb.org
        
        WSGIScriptAlias / "/var/www/MaizeDIG/apache/django.wsgi"
        <Directory "/var/www/MaizeDIG">
            Order allow,deny
            Allow from all
        </Directory>

        ErrorLog logs/MaizeDIG-error_log
        CustomLog logs/MaizeDIG-access_log common
    </VirtualHost>
    ...


