# MaizeDIG: Maize Database of Images and Genomes #

MaizeDIG allows users to tag phenotypes in images and link them to specific genes.
In this document, we focus on the following topics:

* What is prerequisites to set up MaizeDIG?
* How do I get system set up?
* How do I get MaizeDIG set up?
* Deployment Instruction
* Example of usage.


## What is prerequisites to set up MaizeDIG?

There are some prerequisites to set up MaizeDIG system such as installation 
of Django framework, Database system, Python and related libraries, and other dependencies.
Since MaizeDIG is based on [BioDIG](https://github.com/idoerg/BioDIG), 
most of system set up and configurations are followed by BioDIG.
MaizeDIG requires followings:

* Django framework
* ProgreSQL database
* Python and related libraries
* Apache web server
* Chado database schema

MaizeDIG is web-based system and it uses [Django](https://www.djangoproject.com/) 
framework for web development.
In addition, Django framework based on Python.

## How do I get set up?

The summary of set up as follows and we discuss more details in following sub sections.

* Summary of set up
  1. System set up
      - Install Linux (CentOS 7)
      - Firewall set up
      - Webserver (Apache) set up
      - mod-wsgi set up
  2. Installation of Django framework (1.3.7)
      - crete super user for Django
  3. Database set up
      - Install/Configuration PostgreSQL
      - Chado
      - SQLite
  4. Dependencies
      - BioPerl
      - Pip
      - Sorl-thumnail
      - BioPython
      - GFFParser


### System set up

In this project, we used CentOS 7.
If you are not familiar with any Linux system, then we recommend you to install same version of 
Linux system we use to avoid unexpected issues.
Because the most hardest part in system set up is installation/configuration in Linux system.
However, if you have other familiar version of Linux rather than CentOS 7 or 
if you already have your own Linux system, you can use other version as well.

To download CentOS 7, you can use this link [Download CentOS 7](https://www.centos.org/download/).
We skip the details how to install CentOS 7 because it is beyond the scope of this document, 
but you should include at least **Apache web server (Httpd), PostgreSQL database, Python 2.7** 
or above when you install Linux server.
If you are not familiar on installation of Linux, we recommend you to install everything if possible.

Once you have a Linux system, we recommend to create an account for handling maizedig in Linux. 
Following example shows that how to add 'mdig' user account and initialize its password.

> $ sudo adduser mdig
>
> $ sudo passwd mdig


### Django Installation


### Database set up


### Other Dependancies



## Deployment Instructions

1. Clone git repository into /var/www/MaizeDIG/
2. Set proper ownership under /var/www/MaizeDIG/
3. 


## Validation of set up

## Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

## Who do I talk to? ###

* Repo admin: Kyoung Tak Cho
* team contact: MaizeGDB Team