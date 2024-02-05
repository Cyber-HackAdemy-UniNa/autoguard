import 'dart:convert';
import 'dart:typed_data';

import '/flutter_flow/flutter_flow_util.dart';
import 'api_manager.dart';

export 'api_manager.dart' show ApiCallResponse;

const _kPrivateApiFunctionName = 'ffPrivateApiCall';

class GetUserVehiclesCall {
  static Future<ApiCallResponse> call({
    String? idToken = '',
    String? uid = '',
  }) async {
    return ApiManager.instance.makeApiCall(
      callName: 'getUserVehicles',
      apiUrl: 'https://autoguard.website:2053/vehicles',
      callType: ApiCallType.GET,
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ${idToken}',
      },
      params: {
        'uid': uid,
      },
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
      alwaysAllowBody: false,
    );
  }

  static List<String>? model(dynamic response) => (getJsonField(
        response,
        r'''$[:].model''',
        true,
      ) as List?)
          ?.withoutNulls
          .map((x) => castToType<String>(x))
          .withoutNulls
          .toList();
  static List<String>? plateNumber(dynamic response) => (getJsonField(
        response,
        r'''$[:].plateNumber''',
        true,
      ) as List?)
          ?.withoutNulls
          .map((x) => castToType<String>(x))
          .withoutNulls
          .toList();
  static List<String>? vin(dynamic response) => (getJsonField(
        response,
        r'''$[:].vin''',
        true,
      ) as List?)
          ?.withoutNulls
          .map((x) => castToType<String>(x))
          .withoutNulls
          .toList();
  static List<String>? imageLink(dynamic response) => (getJsonField(
        response,
        r'''$[:].imageLink''',
        true,
      ) as List?)
          ?.withoutNulls
          .map((x) => castToType<String>(x))
          .withoutNulls
          .toList();
  static List<String>? id(dynamic response) => (getJsonField(
        response,
        r'''$[:].id''',
        true,
      ) as List?)
          ?.withoutNulls
          .map((x) => castToType<String>(x))
          .withoutNulls
          .toList();
  static List<String>? uid(dynamic response) => (getJsonField(
        response,
        r'''$[:].uid''',
        true,
      ) as List?)
          ?.withoutNulls
          .map((x) => castToType<String>(x))
          .withoutNulls
          .toList();
}

class PostNewVehicleCall {
  static Future<ApiCallResponse> call({
    String? vin = '',
    String? model = '',
    String? plateNumber = '',
    FFUploadedFile? image,
    String? idToken = '',
    String? uid = '',
    FFUploadedFile? token,
  }) async {
    return ApiManager.instance.makeApiCall(
      callName: 'postNewVehicle',
      apiUrl: 'https://autoguard.website:2053/associate',
      callType: ApiCallType.POST,
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ${idToken}',
      },
      params: {
        'image': image,
        'vin': vin,
        'model': model,
        'plateNumber': plateNumber,
        'uid': uid,
        'id_token': idToken,
        'token': token,
      },
      bodyType: BodyType.MULTIPART,
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
      alwaysAllowBody: false,
    );
  }
}

class SetDoorsCall {
  static Future<ApiCallResponse> call({
    String? idToken = '',
    String? id = '',
    String? opened = '',
    String? side = '',
  }) async {
    final ffApiRequestBody = '''
{
  "side": "${side}",
  "opened": "${opened}",
  "id": "${id}"
}''';
    return ApiManager.instance.makeApiCall(
      callName: 'setDoors',
      apiUrl: 'https://autoguard.website:2053/vehicles/rpc/doors',
      callType: ApiCallType.POST,
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ${idToken}',
      },
      params: {},
      body: ffApiRequestBody,
      bodyType: BodyType.JSON,
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
      alwaysAllowBody: false,
    );
  }
}

class SetHeadlightsCall {
  static Future<ApiCallResponse> call({
    String? idToken = '',
    String? opened = '',
    String? id = '',
  }) async {
    final ffApiRequestBody = '''
{
  "opened": "${opened}",
  "id": "${id}"
}''';
    return ApiManager.instance.makeApiCall(
      callName: 'setHeadlights',
      apiUrl: 'https://autoguard.website:2053/vehicles/rpc/headlights',
      callType: ApiCallType.POST,
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ${idToken}',
      },
      params: {},
      body: ffApiRequestBody,
      bodyType: BodyType.JSON,
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
      alwaysAllowBody: false,
    );
  }
}

class ApiPagingParams {
  int nextPageNumber = 0;
  int numItems = 0;
  dynamic lastResponse;

  ApiPagingParams({
    required this.nextPageNumber,
    required this.numItems,
    required this.lastResponse,
  });

  @override
  String toString() =>
      'PagingParams(nextPageNumber: $nextPageNumber, numItems: $numItems, lastResponse: $lastResponse,)';
}

String _serializeList(List? list) {
  list ??= <String>[];
  try {
    return json.encode(list);
  } catch (_) {
    return '[]';
  }
}

String _serializeJson(dynamic jsonVar, [bool isList = false]) {
  jsonVar ??= (isList ? [] : {});
  try {
    return json.encode(jsonVar);
  } catch (_) {
    return isList ? '[]' : '{}';
  }
}
