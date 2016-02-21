angular.module 'upc'
  .factory 'Plan', (API, $resource) ->
    'ngInject'

    resource = $resource API + 'to/', null

    return {
      query: (from_airport, to_city, to_country, in_time, out_time) ->
        resource.query({
          start_city: from_airport,
          event_city: to_city,
          event_country: to_country
          in_time: out_time
          out_time: in_time
        })
    }

