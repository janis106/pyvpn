
class OpenVpnException(Exception):
    pass

class OpenVpnClient:
    pass

class OpenVpnService:
    pass

if __name__ == '__main__':

    vpnsvc = OpenVpnService(config, refresh_site_addresses_on_connect=True)
    vpnsvc.lock_network()

    while do_run():
        try:
            with vpnsvc.connect(site_key, allow_site_dns_lookup=False) as client:
                with client.iptables_setup() as ipt:
                    ipt.add(input, some, rule)
                    ipt.add(output, some, rule)
                execute_whatever()

        except OpenVpnException as exc:
            print(exc)
