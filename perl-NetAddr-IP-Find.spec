#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	NetAddr
%define	pnam	IP-Find
Summary:	NetAddr::IP::Find - Find IP addresses in plain text
Summary(pl.UTF-8):   NetAddr::IP::Find - znajdowanie adresów IP w czystym tekście
Name:		perl-NetAddr-IP-Find
Version:	0.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5f593c24e3edf7ceba7547d0a4cc1068
URL:		http://search.cpan.org/dist/NetAddr-IP-Find/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-NetAddr-IP
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a module for finding IP addresses in plain text.

%description -l pl.UTF-8
Ten moduł służy do znajdowania adresów IP w czystym tekście.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/NetAddr/IP/*.pm
%{_mandir}/man3/*
