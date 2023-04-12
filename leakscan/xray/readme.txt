XRAY Web Vulnerability Scanner Linux amd64 -Zen
"A comprehensive security assessment tool that supports common web security
issue scanning and custom poc"


INSTRUCTIONS

This is a cracked command line tool that does not require installation.  However,
there are a lot of options and for best results you should learn a little about
it and properly configure it for your needs.  Here is some of my top advice:

0. License file not needed.  You can optionally add one and it'll work too.

1. Minor point, but you have to run the tool at least once to generate the default
config file and the certificates.  It does this automatically.  When you see the
error just run it a second time to see usage instructions.

2. You get better results when you use the browser crawler than with the basic one.
This is a Pro feature but with the crack you are good to go.  You need "rad"
(included) and chrome (you need to install it if you haven't).  To use this power
you just specify "--browser" then the URL, and xray will use chrome headless to
crawl the target.
SPECIAL LINUX CHROME INFORMATION:  If your linux install is like mine, you will
have a problem with chrome not wanting to run as root unless you bypass the
sandbox.  Doesn't make a lick of sense to me, and there is probably a great
solution, but the only thing I know to do is edit the bash file to change then
chrome is called such that it includes the --no-sandbox parameter.
Depending on where your chrome is, maybe edit this /usr/bin/google-chrome
so that the line has --no-sandbox, like this (example only!)
  exec -a "$0" "$HERE/chrome" "$@" --user-data-dir --no-sandbox

3. There are a lot of security checks that require the target to be able to 
connect back out to you.  It is the only way those bugs can be tested (the
target web server needs to connect somewhere - sometimes this can be a dedicated
collector like what burpsuite or nuclei use, but here it is a server you run
as part of xray).  In order to enable all those exploit checks you need to set
the reverse server IP in the config file.  If you don't, xray will tell you
what modules it had to disable because they require the reverse server.  If
you run xray on a vps (you should) then this is the publicly accessible IP interface.
read the docs and edit the yaml file.  If you are using a firewall make sure you
set a rule to allow access to the port.

4. Make sure you specify an output format.  There is html (looks nice but requires
javascript wtf), json (text but needs parsing), and webhooks.  Otherwise you just
get spew on the console and have to catch messages as they fly by.  OH, and
there is *still* no --text-output like the docs claim.  Hasn't been for awhile.

5. Take care if you are scanning sites that matter to you - in default without
changing the settings I scanned a strong vps (nginx webserver) which had 4 cores
and 24gb ram and the scan pegged all four of the cpu's at near 100% (nginx was
fine it was mysql mostly) anyway point is you can accidentally dos a server so
if you are doing professional work or bug bounty you probably want to dial this
back a little and not flood the target off the net.  Warning issued.

I guess that's it. When this first came out I found zeroday RCE with it -
some of the checks are pretty good.  Others will give you some false positives
(in previous versions - dunno about this one yet;)

example usage basic scan without rad/chrome:
  ./xray ws --basic http://example.com --html-output example.html

example usage with rad/chrome:
  ./xray ws --browser https://www.ai.mil/ --json-output algorithmicwarfare.json


changelog for 1.9.4 (translated from chinese)

Update details
plugin update

    Add the XStream scanning plug-in , the support list is as follows (the plug-in needs to open the anti-connection platform)
        CVE-2021-21344
        CVE-2021-21345
        CVE-2021-39141
        CVE-2021-39144
        ...(total 29 plugins)
    The fastjson plugin supports cve-2022-25845 the detection of

POC writing/execution update

    Added a warning message, masters can delete files created by the detection plug-in according to the warning message
    Support adding body when GET, HEAD, OPTION
    Add the compare version function to compare the matched versions
    Add html entity encoding / decoding functions
    Add java deserialization function
    Add hex / hexDecode function

optimize content

    Optimized the vulnerability capture logic of the anti-connection platform and improved the hit rate
    Optimized poc lint to become more user-friendly
    The yaml script supports obtaining the link of the rmi anti-connection platform, please refer to the official document for specific usage
    Optimized the Struts2 detection module, added reverse connection confirmation, and reduced false positives and negatives

Fix POC
Optimized rules, weak rules

poc-yaml-drawio-cve-2022-1713-ssrf
poc-yaml-h3c-cvm-upload-file-upload
poc-yaml-iis-cve-2017-7269
poc-yaml-74cms-sqli-cve-2020-22209
poc-yaml-reporter-file-read
poc-yaml-wanhu-ezoffice-documentedit-sqli
poc-yaml-joomla-cve-2017-8917-sqli
poc-yaml-iis-cve-2017-7269
poc-yaml-emerge-e3-cve-2019-7256
poc-yaml-alibaba-nacos-v1-auth-bypass
poc-yaml-wanhu-ezoffice-documentedit-sqli
poc-yaml-magicflow-gateway-main-xp-file-read
poc-yaml-gitblit-cve-2022-31268
poc-yaml-phpstudy-nginx-wrong-resolve
poc-yaml-confluence-cve-2022-26138
poc-yaml-metinfo-lfi-cnvd-2018-13393
poc-yaml-zabbix-cve-2019-17382
poc-yaml-wordpress-paypal-pro-cve-2020-14092-sqli
poc-yaml-vite-cnvd-2022-44615
poc-yaml-phpmyadmin-cve-2018-12613-file-inclusion
poc-yaml-zabbix-cve-2022-23134
poc-yaml-ametys-cms-cve-2022-26159

Optimized deletion (duplication of functions with xray's general plugin)

poc-yaml-nexusdb-cve-2020-24571-path-traversal
poc-yaml-specoweb-cve-2021-32572-fileread
poc-yaml-tvt-nvms-1000-file-read-cve-2019-20085
poc-yaml-zyxel-vmg1312-b10d-cve-2018-19326-path-traversal

Add harmless treatment

poc-yaml-fanruan-v9-file-upload
poc-yaml-h3c-cvm-upload-file-upload
poc-yaml-seeyon-unauthorized-fileupload
poc-yaml-thinkcmf-write-shell
poc-yaml-wanhu-oa-officeserver-file-upload
poc-yaml-weaver-oa-workrelate-file-upload
poc-yaml-yonyou-grp-u8-file-upload
poc-yaml-yonyou-nc-file-accept-upload
poc-yaml-yonyou-u8c-file-upload
poc-yaml-zhiyuan-oa-wpsassistservlet-file-upload

Added 96 POCs

poc-yaml-ruijie-fileupload-fileupload-rce
poc-yaml-eweaver-oa-mecadminaction-sqlexec
poc-yaml-xxl-job-default-password
poc-yaml-wordpress-plugin-superstorefinder-ssf-social-action-php-sqli
poc-yaml-magento-config-disclosure-info-leak
poc-yaml-ukefu-cnvd-2021-18305-file-read
poc-yaml-ukefu-cnvd-2021-18303-ssrf
poc-yaml-eweaver-eoffice-mainselect-info-leak
poc-yaml-linksys-cnvd-2014-01260
poc-yaml-wordpress-welcart-ecommerce-cve-2022-41840-path-traversal
poc-yaml-jeesite-userfiles-path-traversal
poc-yaml-yongyou-nc-iupdateservice-xxe
poc-yaml-v-sol-olt-platform-unauth-config-download
poc-yaml-ibm-websphere-portal-hcl-cve-2021-27748-ssrf
poc-yaml-yonyou-nc-uapws-db-info-leak
poc-yaml-yonyou-nc-service-info-leak
poc-yaml-yongyou-nc-cloud-fs-sqli
poc-yaml-finecms-filedownload
poc-yaml-weaver-eoffice-userselect-unauth
poc-yaml-fortinet-cve-2022-40684-auth-bypass
poc-yaml-dapr-dashboard-cve-2022-38817-unauth
poc-yaml-wordpress-zephyr-project-manager-cve-2022-2840-sqli
poc-yaml-jira-cve-2022-39960-unauth
poc-yaml-qnap-cve-2022-27593-fileupload
poc-yaml-wordpress-all-in-one-video-gallery-cve-2022-2633-lfi
poc-yaml-atlassian-bitbucket-archive-cve-2022-36804-remote-command-exec
poc-yaml-wordpress-simply-schedule-appointments-cve-2022-2373-unauth
poc-yaml-zoho-manageengine-opmanager-cve-2022-36923
poc-yaml-red-hat-freeipa-cve-2022-2414-xxe
poc-yaml-wavlink-cve-2022-2488-rce
poc-yaml-wavlink-cve-2022-34045-info-leak
poc-yaml-wordpress-shareaholic-cve-2022-0594-info-leak
poc-yaml-wordpress-wp-stats-manager-cve-2022-33965-sqli
poc-yaml-opencart-newsletter-custom-popup-sqli
poc-yaml-wordpress-events-made-easy-cve-2022-1905-sqli
poc-yaml-wordpress-kivicare-cve-2022-0786-sqli
poc-yaml-wordpress-cve-2022-1609-rce
poc-yaml-solarview-compact-cve-2022-29303-rce
poc-yaml-wordpress-arprice-lite-cve-2022-0867-sqli
poc-yaml-wordpress-fusion-cve-2022-1386-ssrf
poc-yaml-wordpress-nirweb-cve-2022-0781-sqli
poc-yaml-wordpress-metform-cve-2022-1442-info-leak
poc-yaml-wordpress-mapsvg-cve-2022-0592-sqli
poc-yaml-wordpress-badgeos-cve-2022-0817-sqli
poc-yaml-wordpress-daily-prayer-time-cve-2022-0785-sqli
poc-yaml-wordpress-woo-product-table-cve-2022-1020-rce
poc-yaml-wordpress-documentor-cve-2022-0773-sqli
poc-yaml-wordpress-multiple-shipping-address-woocommerce-cve-2022-0783-sqli
poc-yaml-gitlab-cve-2022-1162-hardcoded-password
poc-yaml-thinkphp-cve-2022-25481-info-leak
poc-yaml-wordpress-cve-2022-0591-ssrf
poc-yaml-wordpress-simple-link-directory-cve-2022-0760-sqli
poc-yaml-wordpress-ti-woocommerce-wishlist-cve-2022-0412-sqli
poc-yaml-wordpress-notificationx-cve-2022-0349-sqli
poc-yaml-wordpress-page-views-count-cve-2022-0434-sqli
poc-yaml-wordpress-masterstudy-lms-cve-2022-0441-unauth
poc-yaml-wordpress-seo-cve-2021-25118-info-leak
poc-yaml-wordpress-perfect-survey-cve-2021-24762-sqli
poc-yaml-wordpress-asgaros-forum-cve-2021-24827-sqli
poc-yaml-tcexam-cve-2021-20114-info-leak
poc-yaml-wordpress-woocommerce-cve-2021-32789-sqli
poc-yaml-wordpress-profilepress-cve-2021-34621-unauth
poc-yaml-wordpress-wp-statistics-cve-2021-24340-sqli
poc-yaml-voipmonitor-cve-2021-30461-rce
poc-yaml-rocket-chat-cve-2021-22911-nosqli
poc-yaml-pega-infinity-cve-2021-27651-unauth
poc-yaml-wordpress-modern-events-calendar-lite-cve-2021-24146-info-leak
poc-yaml-afterlogic-webmail-cve-2021-26294-path-traversal
poc-yaml-wavlink-cve-2020-13117-rce
poc-yaml-prestashop-cve-2021-3110-sqli
poc-yaml-cockpit-cve-2020-35847-nosqli
poc-yaml-cockpit-cve-2020-35848-nosqli
poc-yaml-keycloak-cve-2020-10770-ssrf
poc-yaml-prestashop-cve-2020-26248-sqli
poc-yaml-wordpress-paypal-pro-cve-2020-14092-sqli
poc-yaml-microstrategy-cve-2020-11450-info-leak
poc-yaml-adobe-experience-manager-cve-2019-8086-xxe
poc-yaml-blogengine-net-cve-2019-10717-path-traversal
poc-yaml-dotcms-cve-2018-17422-url-redirection
poc-yaml-php-proxy-cve-2018-19458-fileread
poc-yaml-circarlife-scada-cve-2018-16671-info-leak
poc-yaml-circarlife-scada-cve-2018-16670-info-leak
poc-yaml-circarlife-scada-cve-2018-16668-info-leak
poc-yaml-dotnetnuke-cve-2017-0929-ssrf
poc-yaml-orchid-core-vms-cve-2018-10956-path-traversal
poc-yaml-circarlife-scada-cve-2018-12634-info-leak
poc-yaml-nuuo-nvrmini2-cve-2018-11523-upload
poc-yaml-jolokia-cve-2018-1000130-code-injection
poc-yaml-fiberhome-cve-2017-15647-path-traversal
poc-yaml-opendreambox-cve-2017-14135-rce
poc-yaml-sap-cve-2017-12637-fileread
poc-yaml-glassfish-cve-2017-1000029-lfi
poc-yaml-boa-cve-2017-9833-fileread
poc-yaml-mantisbt-cve-2017-7615-unauth
poc-yaml-wordpress-cve-2017-5487-info-leak
poc-yaml-thinkcmf-cve-2018-19898-sqli


enjoy!
