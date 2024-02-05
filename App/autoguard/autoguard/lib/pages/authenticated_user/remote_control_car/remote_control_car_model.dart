import '/auth/firebase_auth/auth_util.dart';
import '/backend/api_requests/api_calls.dart';
import '/flutter_flow/flutter_flow_icon_button.dart';
import '/flutter_flow/flutter_flow_theme.dart';
import '/flutter_flow/flutter_flow_util.dart';
import '/flutter_flow/flutter_flow_widgets.dart';
import 'remote_control_car_widget.dart' show RemoteControlCarWidget;
import 'package:flutter/material.dart';
import 'package:flutter/scheduler.dart';
import 'package:flutter/services.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:provider/provider.dart';

class RemoteControlCarModel extends FlutterFlowModel<RemoteControlCarWidget> {
  ///  State fields for stateful widgets in this page.

  final unfocusNode = FocusNode();
  // Stores action output result for [Backend Call - API (setDoors)] action in remoteControlCar widget.
  ApiCallResponse? apiResultp01;
  // Stores action output result for [Backend Call - API (setDoors)] action in openLeftDoor widget.
  ApiCallResponse? apiResultimv;
  // Stores action output result for [Backend Call - API (setDoors)] action in closeLeftDoor widget.
  ApiCallResponse? apiResultqqh;
  // Stores action output result for [Backend Call - API (setDoors)] action in IconButton widget.
  ApiCallResponse? apiResultoma;
  // Stores action output result for [Backend Call - API (setDoors)] action in IconButton widget.
  ApiCallResponse? apiResult5z7;
  // Stores action output result for [Backend Call - API (setHeadlights)] action in setHeadlightsOn widget.
  ApiCallResponse? apiResultxtp;
  // Stores action output result for [Backend Call - API (setHeadlights)] action in setHeadlightsOff widget.
  ApiCallResponse? apiResultlvi;

  /// Initialization and disposal methods.

  void initState(BuildContext context) {}

  void dispose() {
    unfocusNode.dispose();
  }

  /// Action blocks are added here.

  /// Additional helper methods are added here.
}
