Summary:	Commons Lang - utility functions and components
Summary(pl.UTF-8):	Commons Lang - funkcje i komponenty narzędziowe
Name:		java-commons-lang
Version:	2.1
Release:	2
License:	Apache v1.1
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/commons/lang/source/commons-lang-%{version}-src.tar.gz
# Source0-md5:	d8379e93f597b2ae6d1f7b4bb7e83fce
URL:		http://commons.apache.org/lang/
BuildRequires:	ant >= 1.5
BuildRequires:	jaxp_parser_impl
BuildRequires:	jpackage-utils
BuildRequires:	rpmbuild(macros) >= 1.294
Requires:	jre
Obsoletes:	jakarta-commons-lang
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Commons Lang is a set of utility functions and reusable
components that should be a help in any Java environment.

%description -l pl.UTF-8
Commons Lang to zestaw funkcji narzędziowych i komponentów
wielokrotnego użycia, które mogą być pomocne w każdym środowisku Javy.

%prep
%setup -q -n commons-lang-%{version}

%build
%ant dist

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

install dist/*.jar $RPM_BUILD_ROOT%{_javadir}
ln -sf commons-lang-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/commons-lang.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt PROPOSAL.html RELEASE-NOTES.txt STATUS.html dist/docs/api
%{_javadir}/*.jar
