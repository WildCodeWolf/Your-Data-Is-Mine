# Description

Feature importance analysis on network traffic dataset.

---

# Goal

Which are the most informative columns to the target value?
Does the time column contribute significant information to the target column?
Can accuracy or fbeta be increased by removing any of the less
informative columns from the models' training?

model score on training data: 0.9999991250841013<br/>
model score on testing data: 0.9999584901294972<br/>

All features - Accuracy: 0.9999584901294972, F-beta Score (beta=10): 0.9157005738871657<br/>

Least important features: ['service_http_8001', 'num_outbound_cmds', 'service_http_2784', 'service_courier', 'service_Z39_50', 'service_netbios_ns', 'service_iso_tsap', 'service_aol', 'service_csnet_ns', 'service_exec', 'service_nnsp', 'service_efs', 'service_hostnames', 'is_host_login', 'service_uucp_path', 'service_harvest', 'service_netbios_dgm', 'service_sql_net', 'service_netbios_ssn', 'service_shell']<br/>

Without least important features - Accuracy: 0.9999591706191776, F-beta Score (beta=10): 0.927010959015988<br/>
Important features: ['duration', 'src_bytes', 'dst_bytes', 'land', 'wrong_fragment', 'urgent', 'hot', 'num_failed_logins', 'logged_in', 'num_compromised', 'root_shell', 'su_attempted', 'num_root', 'num_file_creations', 'num_shells', 'num_access_files', 'is_guest_login', 'count', 'srv_count', 'serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate', 'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count', 'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'dst_host_rerror_rate', 'dst_host_srv_rerror_rate', 'protocol_type_icmp', 'protocol_type_tcp', 'protocol_type_udp', 'service_IRC', 'service_X11', 'service_auth', 'service_bgp', 'service_ctf', 'service_daytime', 'service_discard', 'service_domain', 'service_domain_u', 'service_echo', 'service_eco_i', 'service_ecr_i', 'service_finger', 'service_ftp', 'service_ftp_data', 'service_gopher', 'service_http', 'service_http_443', 'service_imap4', 'service_klogin', 'service_kshell', 'service_ldap', 'service_link', 'service_login', 'service_mtp', 'service_name', 'service_netstat', 'service_nntp', 'service_ntp_u', 'service_other', 'service_pm_dump', 'service_pop_2', 'service_pop_3', 'service_printer', 'service_private', 'service_red_i', 'service_remote_job', 'service_rje', 'service_smtp', 'service_ssh', 'service_sunrpc', 'service_supdup', 'service_systat', 'service_telnet', 'service_tftp_u', 'service_tim_i', 'service_time', 'service_urh_i', 'service_urp_i', 'service_uucp', 'service_vmnet', 'service_whois', 'flag_OTH', 'flag_REJ', 'flag_RSTO', 'flag_RSTOS0', 'flag_RSTR', 'flag_S0', 'flag_S1', 'flag_S2', 'flag_S3', 'flag_SF', 'flag_SH']<br/>

---

# Owner
Nilgün
