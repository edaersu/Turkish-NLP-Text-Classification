import 'dart:convert';
import 'dart:io';

import 'package:csv/csv.dart';
import 'package:flutter/material.dart';
import 'dart:async' show Future;
import 'package:flutter/services.dart' show rootBundle;
import 'package:http/http.dart' as http;

class TableLayout extends StatefulWidget {
  @override
  _TableLayoutState createState() =>
      _TableLayoutState() ?? CircularProgressIndicator();
}

int row = 0;

class _TableLayoutState extends State<TableLayout> {
  List<List<dynamic>> data = [];

  TextEditingController myController = TextEditingController();
  String baslanilacak = '';
  loadAsset() async {
    try {
      final myData = await rootBundle.loadString("assets/res/github.csv");
      List<List<dynamic>> csvTable = CsvToListConverter().convert(myData);
      data = csvTable;
      setState(() {});
    } catch (e) {}
  }

  @override
  void initState() {
    // TODO: implement initState
    loadAsset();
  }

  Future<http.Response> createTicket(
      String satir, String aciliyet, String duygu) async {
    String jsonn2 =
        '{"$satir": {"id": "$satir", "aciliyet": "$aciliyet","duygu":"$duygu"}}';

    var url = 'url';
    var response = await http.post(url, body: jsonn2);
    print('Response status: ${response.statusCode}');
    print('Response body: ${response.body}');
  }

  @override
  Widget build(BuildContext context) {
    int aciliyet = 0;
    String duygu = "";
    return Scaffold(
      appBar: AppBar(
        actions: [
          Container(
            padding: EdgeInsets.only(left: 15),
            margin: EdgeInsets.only(right: 25),
            decoration: BoxDecoration(
                border: Border.all(color: Colors.white),
                borderRadius: BorderRadius.circular(15)),
            child: Row(
              children: [
                SizedBox(
                  width: 100,
                  height: 70,
                  child: TextField(
                      controller: myController,
                      onChanged: (text) {
                        setState(() {
                          baslanilacak = text;
                          print(baslanilacak);
                          row = int.parse(baslanilacak);
                          //you can access nameController in its scope to get
                          // the value of text entered as shown below
                          //UserName = nameController.text;
                        });
                      }),
                ),
              ],
            ),
          ),
          IconButton(
            icon: Icon(Icons.skip_next),
            onPressed: () {
              setState(() {
                createTicket(row.toString(), "pas", "pas");
                row++;
              });
            },
          )
        ],
        title: Text("Labeling"),
      ),
      body: SingleChildScrollView(
          child: Container(
              margin: EdgeInsets.all(15),
              child: Column(
                children: [
                  Container(
                    padding: EdgeInsets.all(5),
                    decoration: BoxDecoration(
                        border: Border.all(color: Colors.black),
                        borderRadius: BorderRadius.circular(15)),
                    child: Text(
                      row.toString(),
                      style: TextStyle(fontSize: 15),
                    ),
                  ),
                  Text(
                    data[0][row],
                    style: TextStyle(fontSize: 15),
                  ),
                  Container(
                    margin: EdgeInsets.only(top: 40),
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.spaceAround,
                      children: [
                        Column(
                          children: [
                            SizedBox(
                              width: 89,
                              height: 89,
                              child: FloatingActionButton(
                                splashColor: Colors.black,
                                backgroundColor: Color(0xffF10000),
                                child: Text(
                                  "ACİL 1",
                                ),
                                onPressed: () {
                                  aciliyet = 1;
                                },
                              ),
                            ),
                            SizedBox(
                              height: 15,
                            ),
                            SizedBox(
                              width: 89,
                              height: 89,
                              child: FloatingActionButton(
                                splashColor: Colors.black,
                                backgroundColor: Color(0xffFF3E3E),
                                child: Text(
                                  "ACİL 2",
                                ),
                                onPressed: () {
                                  aciliyet = 2;
                                },
                              ),
                            ),
                            SizedBox(
                              height: 15,
                            ),
                            SizedBox(
                              width: 89,
                              height: 89,
                              child: FloatingActionButton(
                                splashColor: Colors.black,
                                backgroundColor: Color(0xffFF7878),
                                child: Text(
                                  "ACİL 3",
                                ),
                                onPressed: () {
                                  aciliyet = 3;
                                },
                              ),
                            ),
                            SizedBox(
                              height: 15,
                            ),
                            SizedBox(
                              width: 89,
                              height: 89,
                              child: FloatingActionButton(
                                splashColor: Colors.black,
                                backgroundColor: Colors.grey[400],
                                child: Text(
                                  "ACİL DEĞİL",
                                ),
                                onPressed: () {
                                  aciliyet = 0;
                                },
                              ),
                            ),
                          ],
                        ),
                        Container(
                          margin: EdgeInsets.only(top: 60),
                          child: Column(
                            mainAxisAlignment: MainAxisAlignment.spaceBetween,
                            children: [
                              SizedBox(
                                width: 89,
                                height: 89,
                                child: FloatingActionButton(
                                  splashColor: Colors.black,
                                  backgroundColor: Colors.lightBlue[900],
                                  child: Text(
                                    "Negatif",
                                  ),
                                  onPressed: () {
                                    setState(() {
                                      duygu = "neg";
                                      postDb(row, aciliyet, duygu);
                                    });
                                  },
                                ),
                              ),
                              SizedBox(
                                height: 15,
                              ),
                              SizedBox(
                                width: 89,
                                height: 89,
                                child: FloatingActionButton(
                                  splashColor: Colors.black,
                                  backgroundColor: Colors.grey[400],
                                  child: Text(
                                    "Notr",
                                  ),
                                  onPressed: () {
                                    setState(() {
                                      duygu = "notr";
                                      postDb(row, aciliyet, duygu);
                                    });
                                  },
                                ),
                              ),
                              SizedBox(
                                height: 15,
                              ),
                              SizedBox(
                                width: 89,
                                height: 89,
                                child: FloatingActionButton(
                                  splashColor: Colors.black,
                                  backgroundColor: Colors.green,
                                  child: Text(
                                    "Pozitif",
                                  ),
                                  onPressed: () {
                                    setState(() {
                                      duygu = "pos";
                                      postDb(row, aciliyet, duygu);
                                    });
                                  },
                                ),
                              ),
                            ],
                          ),
                        )
                      ],
                    ),
                  ),
                ],
              ))),
    );
  }

  void postDb(int satir, int aciliyet, String duygu) {
    ///
    ///{  "id":"1245", "aciliyet":"2", "duygu":"neg"  }
    createTicket(satir.toString(), aciliyet.toString(), duygu);
    print("satır: " +
        satir.toString() +
        "    " +
        aciliyet.toString() +
        " duygu: " +
        duygu);
    row++;
  }
}
