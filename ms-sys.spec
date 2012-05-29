Summary:	Create DOS/MS-compatible boot records
Name:		ms-sys
Version:	2.3.0
Release:	1
License:	GPLv2
Group:		System/Configuration/Boot and Init 
URL:		http://ms-sys.sourceforge.net/
Source0:	http://dl.sf.net/ms-sys/ms-sys-%{version}.tar.gz
BuildRequires:	bash
BuildRequires:	gettext

%description
This program is used to create DOS/MS-compatible boot records. It is
able to do the same as Microsoft "fdisk /mbr" to a hard disk. It is
also able to do the same as DOS "sys" to a floppy or FAT32 partition
except that it does not copy any system files, only the boot record is
written.

%prep
%setup -q

%build
%make debug \
	SHELL="/bin/bash" \
	PREFIX="%{_prefix}" \
	CC="${CC:-%{__cc}}" \
	EXTRA_CFLAGS="%{optflags} -fasm" \
	EXTRA_LDFLAGS="%{optflags}"

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc CHANGELOG CONTRIBUTORS COPYING README TODO
%{_bindir}/ms-sys
%doc %{_mandir}/man1/ms-sys.1*

