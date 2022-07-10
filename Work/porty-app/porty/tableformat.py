# tableformat.py

class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plaintext format.
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ') * len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in HTML format.
    '''
    def headings(self, headers):
        print('<tr><th>' + '</th><th>'.join(headers) + '</th></tr>')

    def row(self, rowdata):
        print('<tr><td>' + '</td><td>'.join(rowdata) + '</td></tr>')

class FormatError(Exception):
    pass # custom exception

def create_formatter(name):
    if name == 'txt':
        formatter = TextTableFormatter()
    elif name == 'csv':
        formatter = CSVTableFormatter()
    elif name == 'html':
        formatter = HTMLTableFormatter()
    else:
        raise FormatError('Unknown table format %s' % name)

    return formatter

def print_table(portfolio, columns, formatter):
    '''
    Print out  table.
    '''
    formatter.headings(columns)
    for obj in portfolio:
        rowdata = [str(getattr(obj, name)) for name in columns ]
        formatter.row(rowdata)
