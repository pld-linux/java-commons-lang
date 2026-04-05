#
# Conditional build:
%bcond_without	javadoc		# don't build apidocs
%bcond_with	java_sun	# build with java-sun

%{?use_default_jdk:%use_default_jdk 8}

%define		srcname	commons-lang
Summary:	Commons Lang - utility functions and components
Summary(pl.UTF-8):	Commons Lang - funkcje i komponenty narzędziowe
Name:		java-commons-lang
Version:	2.6
Release:	2
License:	Apache v2.0
Group:		Libraries/Java
Source0:	https://archive.apache.org/dist/commons/lang/source/commons-lang-%{version}-src.tar.gz
# Source0-md5:	37ee469f4caff6cfa28f9d0a0be2d4d2
URL:		http://commons.apache.org/lang/
BuildRequires:	ant >= 1.5
BuildRequires:	java(jaxp_parser_impl)
%buildrequires_jdk
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.556
Obsoletes:	jakarta-commons-lang
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Commons Lang is a set of utility functions and reusable components
that should be a help in any Java environment.

%description -l pl.UTF-8
Commons Lang to zestaw funkcji narzędziowych i komponentów
wielokrotnego użycia, które mogą być pomocne w każdym środowisku Javy.

%package javadoc
Summary:	Online manual for Commons Lang
Summary(pl.UTF-8):	Dokumentacja online do Commons Lang
Group:		Documentation
Requires:	jpackage-utils
Obsoletes:	jakarta-commons-lang-javadoc

%description javadoc
Documentation for Commons Lang.

%description javadoc -l pl.UTF-8
Dokumentacja do Commons Lang.

%description javadoc -l fr.UTF-8
Javadoc pour Commons Lang.

%prep
%setup -q -n commons-lang-%{version}-src

%build

%ant jar %{?with_javadoc:javadoc} \
  -Dcompile.source=1.4 \
  -Dcompile.target=1.4

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

cp -a target/%{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}-%{version}.jar
ln -sf %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}.jar

# javadoc
%if %{with javadoc}
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
cp -a target/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
ln -s %{srcname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{srcname} # ghost symlink
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{srcname}-%{version} %{_javadocdir}/%{srcname}

%files
%defattr(644,root,root,755)
%doc PROPOSAL.html RELEASE-NOTES.txt
%{_javadir}/*.jar

%if %{with javadoc}
%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{srcname}-%{version}
%ghost %{_javadocdir}/%{srcname}
%endif
