ansible-playbook -i /home/mercadmin/ansible/windows_lab_v1/inventory /home/mercadmin/ansible/windows_lab_v1/labplaybooks/win_core_update.yml -vv
ansible-playbook -i /home/mercadmin/ansible/windows_lab_v1/inventory /home/mercadmin/ansible/windows_lab_v1/labplaybooks/win_sec_update.yml -vv
ansible-playbook -i /home/mercadmin/ansible/windows_lab_v1/inventory /home/mercadmin/ansible/windows_lab_v1/labplaybooks/win_app_update.yml -vv
ansible-playbook -i /home/mercadmin/ansible/centos_lab_v1/inventory /home/mercadmin/ansible/centos_lab_v1/labplaybooks/centos_knl_upgrade.yml -vv
ansible-playbook -i /home/mercadmin/ansible/centos_lab_v1/inventory /home/mercadmin/ansible/centos_lab_v1/labplaybookscentos_pkg_upgrade.yml -vv
ansible-playbook -i /home/mercadmin/ansible/centos_lab_v1/inventory /home/mercadmin/ansible/ubtuntu_lab_v2/labplaybooks/ubuntu_upgrade.yml -vv
