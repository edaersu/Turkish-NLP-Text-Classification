import 'package:flutter/material.dart';
import 'package:labeling/csv.dart';

main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: TableLayout() ?? CircularProgressIndicator(),
    );
  }
}
