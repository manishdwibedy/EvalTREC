
# Directory where the data is present
DATA_DIR = '/Users/manishdwibedy/PycharmProjects/MIME/final/'

# Solr Constants
SOLR_HOSTNAME = 'localhost'
SOLR_PORT = 8983
SOLR_CORE = 'mime'

FILE_SIZE = [
    '0 TO 10000',
    '10000 TO 100000',
    '100000 TO 1000000',
    '1000000 TO 10000000',
    '10000000 TO 100000000',
    '100000000 TO *'
]

SIZE_MAPPING = {
    '0 TO 10000' : '0 - 10 KB',
    '10000 TO 100000' : '10 KB - 100 KB',
    '100000 TO 1000000' : '100 KB - 1 MB',
    '1000000 TO 10000000' : '1 MB - 10 MB',
    '10000000 TO 100000000' : '10 MB - 100 MB',
    '100000000 TO *' : '100 MB+'
}

UNITS = ['ft','feet','Euro','f','minutes','miles','beta','mm','degrees','years','cm','M','square meters','megabytes','Mbytes','AU','mm','acres','acres','m','months','degree Fahrenheit','Epoch','nm','degrees','meters','pm','T','watts','days','epsilon','years','megahertz','meter','million km','megawatts','minute','Mg','Mb','km','mintues','kilometers','GB','ft','years','acres','mb','m','km','m','kilometer','moons','million hectares','hPa','cm','calories','inch','kilograms','size','UTC','minute','KH','JT','mile','F','pennies','ton','hours','day','deg','hours','km','kilogram','years','m','nanometers','days','Tg','Tg','F','pounds','kB','hour','hectares','km','bytes','degrees Celcius','db','sq km','nm','km','pm','MB','GHz','m','mb','microns','F','meter','mm','km','HFC','km','minutes','mph','pounds','square feet','ft','mm','impressions','micron','inch','kilogram','mL','miles','gallons','area','inch','years','km','mm','Ph','Pi','volts','minutes','m','hour','miles','Gigabytes','degree','m']