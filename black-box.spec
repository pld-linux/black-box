#
# Conditional build:
%bcond_without	SDL_mixer	# build without SDL_mixer
#
Summary:	Simple logical game
Summary(pl.UTF-8):	Prosta gra logiczna
Name:		black-box
Version:	1.4.7
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://user.cs.tu-berlin.de/~karlb/black-box/%{name}-%{version}.tar.gz
# Source0-md5:	e17d7a0ff13adb690c6eaced99ee4d00
URL:		http://www.linux-games.com/black-box/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_image-devel >= 1.2.0
%{?with_SDL_mixer:BuildRequires:	SDL_mixer-devel >= 1.2.0}
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
You shoot into the black box and you can look where your shots go out
of it. In the box crystals are reflecting your shots. You have to
guess where the are hidden.

%description -l pl.UTF-8
Strzelając do czarnego pudełka, gracz może obserwować, w którym
miejscu pociski z niego wylatują. W pudełku są ukryte kryształy, które
odbijają strzały. Zadaniem gracza jest odnalezienie miejsca ukrycia
każdego kryształu.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
