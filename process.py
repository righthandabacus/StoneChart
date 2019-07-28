table = [[cell.strip() for cell in line.split('\t')] for line in open('data.txt').readlines() if line.strip()]
# label, name, code, begin, end, note

for row in table:
    label,name,code,begin,end,note = row
    name, page = name.rsplit(None,1)
    startx = float(begin) * 10
    try:
        endx = float(end) * 10
    except:
        endx = None
    template_line = r'''
\filldraw[style=%(code)s] (%(startx).2fcm, \curry)--(%(endx).2fcm,\curry) node[align=left, right] {%(label)s:%(name)s${}^{%(page)s}$~} node[black, align=left, below left] {%(ristr)s};
    '''.strip()
    template_circle = r'''
\filldraw[style=%(code)s] (%(startx).2fcm, \curry) circle (0.4mm) node[align=left, right] {%(label)s:%(name)s${}^{%(page)s}$~} node[black, align=left, below left] {%(ristr)s};
    '''.strip()
    template_arrow = r'''
\filldraw[style=%(code)s,->] (%(startx).2fcm, \curry)--(%(endx).2fcm,\curry) node[align=left, right] {%(label)s:%(name)s${}^{%(page)s}$~} node[black, align=left, below left] {%(ristr)s};
    '''.strip()
    if 'OTL' in row:
        if not endx:
            endx = startx+1.0
        if end != 'OTL':
            ristr = begin+'-'+end+' OTL'
        else:
            ristr = begin+'-'+end
        print template_arrow % {'code':code, 'startx':startx, 'endx':endx, 'label':label, 'ristr':ristr, 'name':name, 'page':page}
    elif 'range' in row:
        if not endx:
            endx = startx+1.0
        if end != 'OTL':
            ristr = begin+'-'+end+' OTL'
        else:
            ristr = begin+'-'+end
        print template_line % {'code':code, 'startx':startx, 'endx':endx, 'label':label, 'ristr':ristr, 'name':name, 'page':page}
    else:
        if end:
            ristr = begin+'-'+end
        else:
            ristr = begin
        print template_circle % {'code':code, 'startx':startx, 'label':label, 'ristr':ristr, 'name':name, 'page':page}
    print "\pgfmathparse{\curry+5mm}\edef\curry{\pgfmathresult}"
