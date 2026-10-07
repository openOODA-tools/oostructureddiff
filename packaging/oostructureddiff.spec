Name:           oostructureddiff
Version:        0.1.0
Release:        1%{?dist}
Summary:        AST and JSON structural tree differ highlighting node mutations and key shifts.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oostructureddiff
Source0:        oostructureddiff-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oostructureddiff is a sovereign, capability-bounded TREE DIFFER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oostructureddiff
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oostructureddiff-uninstall

%files
/usr/bin/oostructureddiff
/usr/bin/oostructureddiff-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
