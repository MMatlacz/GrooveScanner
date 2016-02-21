angular.module 'upc'
  .controller 'BookmarkController', ($scope, $rootScope, $sce, $stateParams, $modal, toastr, Airport, Event, Plan) ->
    'ngInject'

    $rootScope.bgstate = 'high'

    $scope.event = null
    $scope.loading_failed = null

    $scope.modal = (plan) ->
      $modal.open
        templateUrl: 'app/views/bookmark_details.html'
        controller: ($scope) ->
          $scope.plan = plan


    $scope.plans = [{"In": "2016-02-28", "Out": "2016-02-27", "Price": 120.0, "QuoteDateTime": "2016-02-20T21:40:00", "hotel": {"address": ", ", "amenities": [11, 17, 6, 15, 5], "distance_from_search": 12.929, "district": 0, "hotel_id": 104477691, "images": {"/10539665/": {"morig.jpg": [5184, 3456], "order": [0], "provider": [177], "rmc.jpg": [628, 418], "rmca.jpg": [627, 470], "rmf.jpg": [2048, 1365], "rmt.jpg": [200, 200]}}, "latitude": 7.120325, "longitude": -73.12418, "name": "Hotel Andino", "number_of_rooms": 0, "popularity": 74, "popularity_desc": "Good", "price": 14, "score": 0, "star_rating": 3, "tag": "AVAILABLE", "types": ["Hotel"]}}, {"In": "2016-02-28", "Out": "2016-02-26", "Price": 124.0, "QuoteDateTime": "2016-02-20T21:40:00", "hotel": {"address": ", ", "amenities": [7, 22, 16, 2, 23, 9, 30, 10, 26, 5], "distance_from_search": 14.328, "district": 0, "hotel_id": 71831195, "images": {"/31769238/": {"morig.jpg": [800, 600], "order": [0], "provider": [28], "rmc.jpg": [626, 470], "rmca.jpg": [627, 470], "rmf.jpg": [800, 600], "rmt.jpg": [200, 200]}}, "latitude": 7.108774, "longitude": -73.11809, "name": "Hotel San Jos\u00e9 Plaza", "number_of_rooms": 0, "popularity": 76, "popularity_desc": "Good", "price": 111, "score": 0, "star_rating": 3, "tag": "AVAILABLE", "types": ["Hotel"]}}, {"In": "2016-02-27", "Out": "2016-02-25", "Price": 146.0, "QuoteDateTime": "2016-02-20T21:19:00", "hotel": {"address": ", ", "amenities": [46, 59, 30, 49, 4, 50, 5, 2, 6, 33, 60, 8, 35, 36, 9, 21, 10, 38, 39, 12, 61, 13, 40, 15, 16, 34, 62, 22, 26, 63, 64, 37, 44, 20, 65, 55, 23, 24, 66, 27], "distance_from_search": 14.476, "district": 0, "hotel_id": 123691678, "images": {"/13346141/": {"morig.jpg": [7051, 3589], "order": [0], "provider": [177], "rmc.jpg": [628, 319], "rmca.jpg": [627, 470], "rmf.jpg": [2048, 1042], "rmt.jpg": [200, 200]}}, "latitude": 7.107837, "longitude": -73.11627, "name": "Hotel Buena Vista Express", "number_of_rooms": 0, "price": 117, "score": 0, "star_rating": 3, "tag": "AVAILABLE", "types": ["Hotel"]}}, {"In": "2016-02-28", "Out": "2016-02-24", "Price": 146.0, "QuoteDateTime": "2016-02-20T18:52:00", "hotel": {"address": ", ", "amenities": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], "distance_from_search": 25.778, "district": 0, "hotel_id": 47019319, "images": {"/25907270/": {"morig.jpg": [2048, 1330], "order": [0], "provider": [112], "rmc.jpg": [628, 407], "rmca.jpg": [627, 470], "rmf.jpg": [2048, 1330], "rmt.jpg": [200, 200]}}, "latitude": 42.18858, "longitude": -79.83233, "name": "Holiday Inn Express Hotel & Suites North East - Erie I-90 Exit 41", "number_of_rooms": 0, "popularity": 90, "popularity_desc": "Excellent", "price": 402, "score": 0, "star_rating": 3, "tag": "AVAILABLE", "types": ["Hotel"]}}]


    Event.get($stateParams.event_id).$promise.then (event) ->
      $scope.event = event
      url = "https:\/\/www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d11972.733584287987!2d" + \
        event.place.location.longitude + "!3d" + event.place.location.latitude + \
        "!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1spl!2ses!4v1456007953889"
      $scope.event_map = $sce.trustAsResourceUrl url

      start_time = event.start_time.split("T")[0]
      end_time = event.end_time.split("T")[0]

      Airport.get($stateParams.airport).$promise.then (airport) ->
        $scope.sourceAirport = airport

        Plan.query(airport.city, airport.country, event.place.location.city, event.place.location.country, \
                    start_time, end_time).$promise.then (data) ->
          $scope.plans = data

    , ->
      $scope.loading_failed = 'Error loading event details. Please try again.'

    @