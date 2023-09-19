**01 What are Transactions**

- Transaction is one of the most important tools that make databases compilant with the ACID-principle

- With a transaction you can isolate your work in a database

- Provides you the capability to string operations together and observe the changes before you either commit or rollback.

- The ACID principle ... (slides)


**01.2 AID**




**Optimistic vs. Pessimistic**

Two-Phase Lock (2PL) is pessimistic in a way that if anything could possibly go wrong, its better to wait

Serializability is pessimistic to the extreme where there is basically only one transaction and one lock per database -> Transactions must be quick

Serializable Snapshot Isolation (SSI) is optimistic and instead of blocking if anything potentially dangerous happen, it continues the transaction and when its ready to commit, it checks if anything bad happened. -> If isolation is violated, transaction must retry or abort

Its not all perfect though, if many transactions are trying to access the same values as then all of these transaction will have to retry causing overhead.

Normal Snapshat Isolation = point in time snapshot of data (back ups)
Serializable Snapshot Isolation = SI with Outdated Premise detection