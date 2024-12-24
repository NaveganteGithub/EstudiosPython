import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

extensiones_archivos = [".3ds", ".ace", ".aif", ".aiff", ".aifc", ".ani", ".arc", ".arj", ".asp", ".avi",
".bak", ".bmp", ".bat", ".bin", ".c", ".csv", ".dll", ".doc", ".docm", ".docx",
".exe", ".flv", ".gif", ".htm", ".html", ".iso", ".jar", ".jpg", ".jpeg", ".mp3",
".flac", ".ogg", ".png", ".jpeg", ".bmp", ".txt", ".doc", ".docx", ".rtf", ".mp4",
".avi", ".mov", ".exe", ".apk", ".264", ".386", ".3dc", ".3dg", ".html",  ".htm",
".css", ".js", ".php", ".asp", ".aspx", ".jsp", ".xml", ".svg", ".json", ".woff", 
".woff2", ".ttf", ".otf", ".eot", ".png", ".jpeg", ".jpg", ".gif", ".ico", ".svg",
".webp", ".mp4", ".webm", ".ogg", ".mp3", ".wav", ".ogg", ".flac", ".bmp", ".gif", 
".heif", ".heic", ".jpg", ".jpeg", ".png", ".psd", ".mp4", ".avi", ".mkv", ".flv",
".mov", ".wmv", ".divx", ".h264", ".xvid", ".rm", ".mp3", ".wav", ".ogg", ".flac", 
".odt", ".ods", ".odp", ".odg", ".odb", ".doc", ".docm", ".docx", ".dot", ".dotm",
".dotx", ".htm", ".html", ".mht", ".mhtml", ".xls", ".xlsx", ".xlsm", ".xlt", ".ppt",
".pptx", ".pps", ".pot", ".doc", ".docx", ".dot", ".dotx", ".htm", ".html", ".mht",
".mhtml", ".rtf", ".csv", ".xls", ".xlsx", ".ppt", ".pptx", ".pdf", ".txt", ".7z",
".ace", ".afa", ".arc", ".ark", ".sue", ".alz", ".cab", ".cfs", ".cpt", ".dar", ".dgc",
".dmg", ".gca", ".hki", ".jar", ".lha", ".lzh", ".lzx", ".partimg", ".pq6", ".qda",
".rar", ".rev", ".r00", ".r01", ".rk", ".sea", ".sit", ".sqx", ".tar.gz", ".tgz", 
".tar.Z", ".tar.bz2", ".tbz2", ".tar.lz", ".tlz", ".zip", ".zoo", ".zz", ".eps",
".pic", ".pct", ".ai", ".cdr", ".cgm", ".dxf", ".dwg", ".eps", ".fh*", ".fla", ".pdf",
".ps", ".svg", ".svgz", ".swf", ".wmf", ".art", ".bmp", ".cin", ".cpt", ".dpx",
".exr", ".fpx", ".gif", ".iff", ".ilbm", ".lbm", ".jpeg", ".jpg", ".jpg2", ".jp2", 
".mng", ".nef", ".pbm", ".pcd", ".pcx", ".pdn", ".pgm", ".png", ".ppm", ".psd",
".psp", ".raw", ".tga", ".tpic", ".tiff", ".tif", ".wbmp", ".xbm", ".xcf", ".xpm",
".a", ".ar", ".cpio", ".shar", ".tar", ".narc", ".arc", ".carc", ".bz2", ".gz",
".lz", ".lzma", ".lzo", ".rz", ".z", ".php", ".phtml", ".php3", ".php4", ".php5", 
".php7", ".phps", ".php-s", ".pht", ".phar", ".3gp", ".7z", ".aac", ".abw", ".ai",
".apk", ".appimage", ".avi", ".bmp", ".bz2", ".cbr", ".cbz", ".cdr", ".cer", ".cgm",
".cmx", ".csv", ".deb", ".dmg", ".doc", ".docx", ".dwg", ".dxf", ".eot", ".epub",
".exe", ".f4v", ".flac", ".flv", ".gif", ".gz", ".h264", ".html", ".ico", ".ics",
".iso", ".jar", ".jpeg", ".jpg", ".js", ".json", ".latex", ".log", ".m4a", ".mdb",
".mid", ".exe", ".bat", ".cmd", ".com1", ".vbs", ".vbe", ".js", ".jse", ".wsf", 
".wsh", ".psc1" ".app2", ".pkg2,", ".sh3" ".bin", ".elf4", ".sh5", ".sh6", ".sh5",
".deb", ".rpm", ".txz", ".snap", ".c", ".cpp", ".cs", ".java", ".py", ".js", ".rb",
".go", ".rs", ".swift", ".php", ".ts", ".m", ".kt", ".scala", ".lua", ".r", ".pl",
".sh", ".sql", ".f", ".p", ".pl", ".m", ".s", ".lisp", ".cls", ".dart", ".groovy",
".hs", ".lua", ".r", ".scala", ".swift", ".ts", ".vbs", ".bat", ".ps1", ".sh",
".sql", ".coffee", ".cfm", ".cfml", ".hpp", ".rb", ".jav", ".c3", ".cc", ".4th",
".gmd", ".nx", ".asvf", ".f", ".p", ".pl", ".m", ".s", ".lisp", ".cls", ".dart",
".groovy", ".hs", ".lua", ".r", ".scala", ".swift", ".ts", ".vbs", ".bat", ".ps1",
".sh", ".sql", ".c", ".cpp", ".cs", ".java", ".py", ".js", ".rb", ".go", ".rs",
".swift", ".php", ".ts", ".m", ".kt", ".scala", ".lua", ".r", ".pl", ".sh", ".sql",
".html", ".htm", ".css", ".scss", ".js", ".mjs", ".php", ".rb", ".rjs", ".py",
".java", ".jsp", ".jspx", ".wss", ".do", ".action", ".cs", ".asax", ".ascx", 
".aspx", ".axd", ".asx", ".asmx", ".ashx", ".ts", ".json", ".xml", ".rss", ".svg",
".sql", ".pl", ".cgi", ".swift", ".kt", ".go", ".shtml", ".cfm", ".yaws", ".swf",
".dll", ".wav", ".aif", ".aiff", ".mp3", ".aac", ".flac", ".m4a", ".wma", ".ogg",
".dsf", ".dff", ".mid", ".midi", ".opus", ".amr", ".au", ".ra", ".rm", ".qcp",
".act", ".dts", ".ac3", ".mmf", ".ape", ".mpc", ".wv", ".tta", ".m4b", ".m4r",
".m4p", ".mp2", ".mp1", ".gsm", ".qcelp", ".vqf", ".ra", ".shn", ".voc", ".caf",
".it", ".xm", ".s3m", ".mtm", ".umx", ".mo3", ".m4a", ".f4a", ".f4b", ".f4p", ".f4v",
".dts", ".cda", ".amr", ".mpc", ".mpp", ".spx", ".tta", ".wv", ".mpc", ".ofr",
".ofs", ".mp1", ".mp2", ".m2a", ".mpa", ".m1a", ".m2a", ".mpa", ".apl", ".mac",
".svx", ".snd", ".sf", ".voc", ".w64", ".mat", ".pvf", ".xi", ".htk", ".caf",
".sd2", ".scd", ".tak", ".ttpl", ".dct", ".gsm", ".msv", ".vms", ".cvu", ".dvf",
".dvr", ".m4b", ".aax", ".aa", ".atrac", ".amr", ".awb", ".dss", ".dvf", ".ics",
".m4p", ".mp9", ".oma", ".voc", ".vox", ".wma", ".txt", ".rtf", ".log", ".doc",
".docx", ".dotx", ".dotm", ".ltx", ".diz", ".wtt", ".dsc", ".docm", ".apt", ".odm", 
".ans", ".lue", ".b", ".eio", ".tmdx", ".gpd", ".readme", ".rst", ".lst", ".asc",
".wpd", ".text", ".wpt", ".tex", ".rpt", ".nfo", ".rft", ".bat", ".cmd", ".ps1",
".vbs", ".js", ".py", ".sh", ".pl", ".rb", ".sh", ".awk", ".sed", ".tcl", ".lua",
".csh", ".ksh", ".zsh"][:7]

extensiones_archivos = set(extensiones_archivos)
extensiones_archivos = sorted(list(extensiones_archivos))
extensiones_archivos = tuple(extensiones_archivos)

# print(extensiones_archivos)

ruta_archivo = "Src\\pyIntelligenceThreat\\"
nombre_archivo = "prueba"
extension_archivo = ".txt"

for e in extensiones_archivos:
    old_path = ruta_archivo + nombre_archivo + extension_archivo
    extension_archivo = e
    new_path = ruta_archivo + nombre_archivo + extension_archivo

    """print("Ciclo: " + e)
    print("Old Path: ", old_path)
    print("New Path: ", new_path)"""

    os.rename(old_path, new_path)
    print(f"El archivo {old_path} a sido renombrado a {new_path}")

browser = webdriver.Firefox()

browser.get('http://annex.uploadvulns.thm')

elem = browser.find_element(By.NAME, '')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)

browser.quit()