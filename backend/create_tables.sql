CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Пользователи и роли
CREATE TABLE IF NOT EXISTS TI (
  Id uuid DEFAULT uuid_generate_v4 () NOT NULL,
  ip VARCHAR(32) NOT NULL,
  PRIMARY KEY (Id)
);
