# GeoDjango
Working with GeoDjango for Spatial Backends in Django using Postgresql

## API Endpoints for Providers and Services by them

### API Endpoints for Providers

#### List all Providers

GET : /api/provider/list/ (<i>return JSON Array of provider objects.</i>)


#### Create Provider

POST : /api/provider/create/

##### Parameters to Pass
1) name : Name of the Provider
2) email : Email ID of the provider
3) phone_number : Phone number of provider in format +987665353 (9-15 characters allowed)
4) language: Provider's language

Current language options below (pass the first parameter in POST)
LANGUAGE_CHOICES = [
    ('USA','ENGLISH-US'),
    ('UK','ENGLISH-UK'),
    ('Japan','JAPANESE'),
    ('China','MANDARIN'),
    ('France', 'FRENCH'),
    ('Germany','GERMAN'),
    ('Portugal','PORTUGUESE'),
    ('Spain','SPANISH')
]

5) currency: Provider's Currency

Current currency options below (pass the first parameter in POST)
CURRENCY_CHOICES = [
    ('Europe','EUR'),
    ('Britain','GBP'),
    ('Japan','JPY'),
    ('USA','USD')
]

#### Edit Provider

PUT : /api/provider/{id}/edit/ (<i>where id is the provider ID and an integer.</i>)

##### Parameters to Pass
1) name : Name of the Provider
2) email : Email ID of the provider
3) phone_number : Phone number of provider in format +987665353 (9-15 characters allowed)
4) language: Provider's language

Current language options below (pass the first parameter in POST)
LANGUAGE_CHOICES = [
    ('USA','ENGLISH-US'),
    ('UK','ENGLISH-UK'),
    ('Japan','JAPANESE'),
    ('China','MANDARIN'),
    ('France', 'FRENCH'),
    ('Germany','GERMAN'),
    ('Portugal','PORTUGUESE'),
    ('Spain','SPANISH')
]

5) currency: Provider's Currency

Current currency options below (pass the first parameter in POST)
CURRENCY_CHOICES = [
    ('Europe','EUR'),
    ('Britain','GBP'),
    ('Japan','JPY'),
    ('USA','USD')
]

#### Delete Provider

DELETE : /api/provider/{id}/delete/ (<i>where id is the provider ID and an integer.</i>)

#### Detail of a Provider

GET : /api/provider/{id}/detail/ (<i>where id is the provider ID and an integer.</i>)


### API Endpoints for Service Areas by Providers

#### List all Services

GET : /api/service/list/ (<i>return JSON Array of service objects.</i>)


#### Create Service

POST : /api/service/create/

##### Parameters to Pass
1) provider : ID of the Provider (Foreign Key)
2) name : Service Name
3) price : Price as Float Value
4) polygon: It defines the polygon inside map. An example polygon parameter will look like following:
"POLYGON ((75.58965426204122 29.17621676045837, 73.91973238704121 26.65244156227428, 77.56719332454122 24.55219433828061, 79.67656832454122 27.70791968504295, 75.58965426204122 29.17621676045837))"

where space separated values are long/lat and comma separated pairs are coordinates of different point on map.

#### Update Service

POST : /api/service/{id}/edit/ (<i>where id is the service ID and an integer.</i>)

##### Parameters to Pass
1) provider : ID of the Provider (Foreign Key)
2) name : Service Name
3) price : Price as Float Value
4) polygon: It defines the polygon inside map. An example polygon parameter will look like following:
"POLYGON ((75.58965426204122 29.17621676045837, 73.91973238704121 26.65244156227428, 77.56719332454122 24.55219433828061, 79.67656832454122 27.70791968504295, 75.58965426204122 29.17621676045837))"

where space separated values are long/lat and comma separated pairs are coordinates of different point on map.

#### Delete Service

DELETE : /api/service/{id}/delete/ (<i>where id is the service ID and an integer.</i>)

#### Detail of a Service

GET : /api/service/{id}/detail/ (<i>where id is the service ID and an integer.</i>)

### API Endpoints for Searching Service Areas by Coordinates

GET : /api/service/{lat,long}/list/ (<i>where {lat,long} is a comma separated string and lat=coordinate's latitude, long = coordinate's longitude.</i>)

It will return all the services areas containing this coordinate.



###END