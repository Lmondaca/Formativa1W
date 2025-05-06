import oracledb

try:
    conn = oracledb.connect(
        user="WEB1",
        password="ClaveOracle123",
        dsn="adb.sa-valparaiso-1.oraclecloud.com:1522/g0022de2e3ebc85_cmb0n6s7y4so8ofj_high.adb.oraclecloud.com",
        ssl_server_cert_dn="CN=adb.sa-valparaiso-1.oraclecloud.com, O=Oracle Corporation, L=Redwood City, ST=California, C=US"
    )
    print("Conexión exitosa!")
except Exception as e:
    print("Error:", e)