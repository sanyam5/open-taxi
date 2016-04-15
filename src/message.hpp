#pragma once

#include <stdio.h>
#include <bits/stdc++.h>

using namespace std;

static const int TIMEOUT = 50; // time for a message to timeout

// data type for any message that is exchanged between two nodes.

enum MType {
  FIND_SUCCESSOR,
  FIND_SUCCESSOR_ANSWER,
  GET_PREDECESSOR,
  GET_PREDECESSOR_ANSWER,
  NOTIFY,
  SUCCESSOR_LEAVING,
  PREDECESSOR_LEAVING,
  PREDECESSOR_ALIVE,
  PREDECESSOR_ALIVE_ANSWER
};


class Message {
public:
  MType type; // type of message
  int request_id;                         // id paramater (used by some types of tasks)
  int request_finger;                     // finger parameter (used by some types of tasks)
  int answer_id;                          // answer (used by some types of tasks)
  char answer_to[200];      // mailbox to send an answer to (if any)
  char issuer_host_name[200];           // used for logging
};


