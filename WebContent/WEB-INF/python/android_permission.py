from xml.dom import minidom


def permission(manifest_file):
    manifest_file_content = minidom.parse(manifest_file)
    root = manifest_file_content.documentElement
    permission_elements = root.getElementsByTagName('uses-permission')
    permissions = []
    for element in permission_elements:
        permissions.append(element.getAttribute('android:name'))
    return permissions


if __name__ == '__main__':
    manifest_file = 'D:\\Analysis\\com.huawei.ipc.apk.jadx.out\\resources\\AndroidManifest.xml'
    permissions = permission(manifest_file)
    print(permissions)