# $Id: perl-Data-Phrasebook-Loader-YAML.spec 7981 2009-11-03 03:05:34Z dag $
# Authority: dries
# Upstream: Barbie <barbie$cpan,org>

%define upstream_name Data-Phrasebook-Loader-YAML

Summary:	Absract your phrases with YAML
Name:		perl-%{upstream_name}
Version:	0.09
Release:	2
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/Data-Phrasebook-Loader-YAML/
Source:		http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::More) >= 0.47
BuildArch:	noarch

%description
Absract your phrases with YAML.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%make

%install
make pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%files
%defattr(-, root, root, 0755)
%doc Artistic COPYING Changes INSTALL LICENSE MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/Data::Phrasebook::Loader::YAML.3pm*
%dir %{perl_vendorlib}/Data/
%dir %{perl_vendorlib}/Data/Phrasebook/
%dir %{perl_vendorlib}/Data/Phrasebook/Loader/
%{perl_vendorlib}/Data/Phrasebook/Loader/YAML.pm


%changelog
* Tue Sep 27 2011 Leonardo Coelho <leonardoc@mandriva.com> 0.09-1mdv2012.0
+ Revision: 701516
- first mandriva version
- Created package structure for 'perl-Data-Phrasebook-Loader-YAML'.

