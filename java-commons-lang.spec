Summary:	Jakarta Commons Lang - utility functions and components
Summary(pl):	Jakarta Commons Lang - funkcje i komponenty narzêdziowe
Name:		jakarta-commons-lang
Version:	1.0.1
Release:	0.1
License:	Apache
Group:		Development/Languages/Java
Source0:	http://jakarta.apache.org/builds/jakarta-commons/release/commons-lang/v1.0.1/commons-lang-%{version}-src.tar.gz
# Source0-md5:	7217632e6a7f18770734128baba273c2
URL:		http://jakarta.apache.org/
BuildRequires:	jakarta-ant >= 1.5
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	%{_datadir}/java

%description
Jakarta Commons Lang is a set of utility functions and reusable
components that should be a help in any Java environment.

%description -l pl
Jakarta Commons Lang to zestaw funkcji narzêdziowych i komponentów
wielokrotnego u¿ycia, które mog± byæ pomocne w ka¿dym ¶rodowisku Javy.

%prep
%setup -q -n commons-lang-%{version}-src

%build
cd lang
cp LICENSE.txt ../LICENSE
ant dist

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javalibdir}

install lang/dist/*.jar $RPM_BUILD_ROOT%{_javalibdir}
ln -sf commons-lang-%{version}.jar $RPM_BUILD_ROOT%{_javalibdir}/commons-lang.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lang/dist/LICENSE lang/dist/RELEASE-NOTES.txt lang/dist/docs/api
%{_javalibdir}/*.jar
