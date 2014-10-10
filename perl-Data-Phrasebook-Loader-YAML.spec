# $Id: perl-Data-Phrasebook-Loader-YAML.spec 7981 2009-11-03 03:05:34Z dag $
# Authority: dries
# Upstream: Barbie <barbie$cpan,org>

%define upstream_name Data-Phrasebook-Loader-YAML
%define upstream_version 0.12

Summary:	Absract your phrases with YAML
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/Data-Phrasebook-Loader-YAML/
Source:		http://www.cpan.org/modules/by-module/Data/Data-Phrasebook-Loader-YAML-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::More) >= 0.47
BuildArch:	noarch

%description
Absract your phrases with YAML.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%make

%install
make pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%files
%defattr(-, root, root, 0755)
%doc Changes INSTALL LICENSE MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/Data::Phrasebook::Loader::YAML.3pm*
%dir %{perl_vendorlib}/Data/
%dir %{perl_vendorlib}/Data/Phrasebook/
%dir %{perl_vendorlib}/Data/Phrasebook/Loader/
%{perl_vendorlib}/Data/Phrasebook/Loader/YAML.pm



