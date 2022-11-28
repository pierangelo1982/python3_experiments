### query test

```
curl -H "Content-Type: application/json" -XGET '192.168.56.1:9200/regioni//_search?q=denominazione_regione:Lombardia
```

```
curl -H "Content-Type: application/json" -XGET '192.168.56.1:9200/regioni//_search?q=denominazione_regione:Lombardia&size=100&pretty'
```


```
curl -H "Content-Type: application/json" -XPOST '192.168.56.1:9200/regioni/_search?pretty' -d '
{
    "query" : {
        "match_all" : {}
    }
}
'
```

```
curl -H "Content-Type: application/json" -XGET '192.168.56.1:9200/regioni/_search?search_type=scan&scroll=10m&size=50&pretty' -d '
{
    "query" : {
        "match_all" : {}
    }
}
'
```

```
curl -H "Content-Type: application/json" -XPOST '192.168.56.1:9200/regioni/_search?pretty' -d '
{
    "query": {
        "match" : {
            "denominazione_regione" : {
                "query" : "Lombardia"
            }
        }
    }
}
'
```

```
curl -H "Content-Type: application/json" -XPOST '192.168.56.1:9200/regioni/_search?pretty' -d '
{
  "query": { 
    "bool": { 
      "must": [
        { "match": { "denominazione_regione": "Lombardia" }}
      ],
      "filter": [ 
        { "range": { "data": { "lte": "2020-03-20" }}}
      ]
    }
  }
}
'
```

```
curl -H "Content-Type: application/json" -XPOST '192.168.56.1:9200/regioni/_search?pretty' -d '
{
  "query": { 
    "bool": { 
      "must": [
        { "match": { "denominazione_regione": "Lombardia" }}
      ],
      "filter": [ 
        { "range": 
            { "data": { "lte": "2020-03-25", "gte": "2020-03-20" }}
        }
      ]
    }
  }
}
'
```


```
curl -H "Content-Type: application/json" -XPOST '192.168.56.1:9200/regioni/_search?pretty' -d '
{
  "query": { 
    "bool": { 
      "must": [
        { "match": { "denominazione_regione": "Lombardia" }}
      ],
      "filter": [ 
        { "range": 
            { "totale_casi": { "lte": "11000", "gte": "2000" }}
        }
      ]
    }
  }
}
'
```