# Team Wins 🎉

### **Performance Pod Sprint Objective - Jan Bernatik**

**Done last sprint**


**This sprint**

- Continue Atree register inlining:
  https://github.com/onflow/atree/issues/292
- Complete data collection of script execution on RN
- Storehouse design (execution state on disk)
- execution state scaling POC: https://github.com/onflow/flow-go/issues/3809
- Investigations:
    - Go Routine Leak
    - Disc space usage

**On Hold**

- Plan removal of concurrent storage bottlenecks
    - Transaction fee deduction
    - [Cadence Type checker is not reentrant](https://dapperlabs.slack.com/archives/CG0B7CJAJ/p1684434997197079) (type comparison depends on consistent pointer used by programs cache, program cache needs to always return the same pointer to the same type)
- https://github.com/onflow/flow-go/issues/3548

**Active Epics**

- https://github.com/onflow/atree/issues/292
- https://github.com/onflow/flow-go/issues/4077

### Cadence

### **Stable Cadence - Jan Bernatik**

<aside>
💡 **Objective:** long-term support release of Cadence with no expected breaking changes

</aside>

**Done last sprint**

**This sprint**

- Bugfixes
    - Internal issue #139
    - https://github.com/onflow/cadence/issues/2458
- Continue work on Stable Cadence preview release
- Continue implementation of Account Type refactoring
    - https://github.com/onflow/cadence/issues/2641
    - https://github.com/onflow/flips/pull/92
- Continuing with Stable Cadence scope / discussions
    - Ongoing FLIPs: [Stable Cadence FLIPs status summary](https://www.notion.so/Stable-Cadence-FLIPs-status-summary-c58a5d5c408047dba59321e4d3a0cef1?pvs=21)
        - [External mutability restrictions](https://www.notion.so/Stable-Cadence-FLIPs-status-summary-c58a5d5c408047dba59321e4d3a0cef1?pvs=21)
        - [Account Type Refactoring](https://github.com/onflow/flips/pull/92)
        - [Removing Type Requirements](https://github.com/onflow/flips/pull/118)
    - Continue to work on a proposal for [Attachments trolling attack](https://www.notion.so/Stable-Cadence-FLIPs-status-summary-c58a5d5c408047dba59321e4d3a0cef1?pvs=21)
    - Resume discussion of the re-entrancy edge cases

**Active Epics**

- https://github.com/dapperlabs/cadence-private-issues/issues/6
    - https://github.com/onflow/cadence/issues/2091
- https://github.com/onflow/cadence/issues/2157


### Access & Data Availability **- Peter Argue**

**Done last sprint**


**This sprint**

- Continue working with KROK on Access PRs
- Archive Node V2
    - Complete script execution validation between RN/ENs
    - https://github.com/onflow/flow-go/issues/4606
- [OKR] Complete Execution Data Improvements
    - https://github.com/onflow/flow-go/issues/2120
    - https://github.com/onflow/flow-go/issues/4455

**Active Epics**

- https://github.com/dapperlabs/flow-internal/issues/1745
- https://github.com/onflow/flow-go/issues/4410

**On Hold**

- [OKR] Working towards Execution data indexer & script execution on Access nodes
    - On hold until Archive V2 work complete
- [OKR] Enable Execution Sync on Public Network
    - On hold until execution data improvements are complete

### **Permissionless Network - Kan Zhang**

**Done last sprint**

**This sprint**

- Baseline protections
    - https://github.com/onflow/flow-go/pull/4574
    - https://github.com/dapperlabs/flow-go/issues/6819
    - https://github.com/dapperlabs/flow-internal/issues/1892
    - https://github.com/dapperlabs/flow-go/issues/6472
    - https://github.com/dapperlabs/flow-go/issues/6798

**Active Epics**

- https://github.com/dapperlabs/flow-go/issues/6287
- https://github.com/dapperlabs/flow-go/issues/6468
- BFT https://github.com/dapperlabs/flow-go/issues/6142
- BFT https://github.com/dapperlabs/flow-go/issues/6398
- BN2 https://github.com/dapperlabs/flow-go/issues/6341
- TPS  https://github.com/dapperlabs/flow-go/issues/6296

### Consensus (Dynamic Protocol State) **- Jerome Pimmel**

**Done last sprint**


**This sprint**

- https://github.com/dapperlabs/flow-go/issues/6801
- https://github.com/dapperlabs/flow-go/issues/6802
- https://github.com/dapperlabs/flow-go/issues/5514
- Creating static identity model, a huge refactoring of`flow.Identity`
    - https://github.com/dapperlabs/flow-go/issues/6232
- https://github.com/dapperlabs/flow-go/issues/5529

### **Infra - Sjon-Paul Brown**


**Done last sprint**

**********************This Sprint**********************

******Dapper Flow Node******

- Onboard Dapper nodes to Canary & Devnet

**********************Quick Node**********************

- Assist with Quick Node Migration

************Cast FYI************

- Assist with the deployment & management of Cast FYI

********************Flow DevEx********************

- Discovering & propose solution for migrating away from K8s for DevEx & Cast applications
