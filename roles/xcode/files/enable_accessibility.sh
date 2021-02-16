#!/bin/bash

if test z$1 = z ; then
  echo -e "\n********************************************************************************"
  echo -e "\n           Must pass ansible_distribution_version as an argument"
  echo -e "\n********************************************************************************"
  exit 1
fi

if test "z$1" = "z10.15.6" || test "z$1" = "z10.15.7" ; then
  #schema of the table on Catalina 10.15.6
  #
  #CREATE TABLE access (
  #  service        TEXT        NOT NULL,
  #  client         TEXT        NOT NULL,
  #  client_type    INTEGER     NOT NULL,
  #  allowed        INTEGER     NOT NULL,
  #  prompt_count   INTEGER     NOT NULL,
  #  csreq          BLOB,
  #  policy_id      INTEGER,
  #  indirect_object_identifier_type    INTEGER,
  #  indirect_object_identifier         TEXT,
  #  indirect_object_code_identity      BLOB,
  #  flags          INTEGER,
  #  last_modified  INTEGER     NOT NULL DEFAULT (CAST(strftime('%s','now') AS INTEGER)),
  #  PRIMARY KEY (service, client, client_type, indirect_object_identifier),
  #  FOREIGN KEY (policy_id) REFERENCES policies(id) ON DELETE CASCADE ON UPDATE CASCADE);
  sudo sqlite3 "/Library/Application Support/com.apple.TCC/TCC.db" "INSERT INTO access VALUES('kTCCServiceAccessibility','com.apple.dt.Xcode',0,1,1,'','','','UNUSED','',0,'1606910422');"

elif test "z$1" = "z11.2" ; then
  # schema on Big Sur 11.2
  # CREATE TABLE access (
  # service        TEXT        NOT NULL,
  # client         TEXT        NOT NULL,
  # client_type    INTEGER     NOT NULL,
  # auth_value     INTEGER     NOT NULL,
  # auth_reason    INTEGER     NOT NULL,
  # auth_version   INTEGER     NOT NULL,
  # csreq          BLOB,
  # policy_id      INTEGER,
  # indirect_object_identifier_type    INTEGER,
  # indirect_object_identifier         TEXT NOT NULL DEFAULT 'UNUSED',
  # indirect_object_code_identity      BLOB,
  # flags          INTEGER,
  # last_modified  INTEGER     NOT NULL DEFAULT (CAST(strftime('%s','now') AS INTEGER)),
  # PRIMARY KEY (service, client, client_type, indirect_object_identifier),
  # FOREIGN KEY (policy_id) REFERENCES policies(id) ON DELETE CASCADE ON UPDATE CASCADE);
  sudo sqlite3 "/Library/Application Support/com.apple.TCC/TCC.db" "INSERT INTO access VALUES('kTCCServiceAccessibility','com.apple.dt.Xcode',0,2,4,1,NULL,NULL,0,'UNUSED',NULL,0,0);"
else
  echo -e "\n********************************************************************************"
  echo -e "\n                Unsupported macOS version to enable accessibility"
  echo -e "\n********************************************************************************"
  exit 1
fi
