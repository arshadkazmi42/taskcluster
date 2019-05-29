# coding=utf-8
#####################################################
# THIS FILE IS AUTOMATICALLY GENERATED. DO NOT EDIT #
#####################################################
# noqa: E128,E201
from ...aio.asyncclient import AsyncBaseClient
from ...aio.asyncclient import createApiClient
from ...aio.asyncclient import config
from ...aio.asyncclient import createTemporaryCredentials
from ...aio.asyncclient import createSession
_defaultConfig = config


class WorkerManagerEvents(AsyncBaseClient):
    """
    These exchanges provide notifications when a worker pool is created, updatedor deleted. This is so that the listener running in a differentprocess at the other end can synchronize its bindings. But you are ofcourse welcome to use these for other purposes, monitoring changes for example.
    """

    classOptions = {
        "exchangePrefix": "exchange/taskcluster-worker-manager/v1/",
    }
    serviceName = 'worker-manager'
    apiVersion = 'v1'

    def workerPoolCreated(self, *args, **kwargs):
        """
        Worker Pool Created Messages

        Whenever the api receives a request to create aworker pool, a message is posted to this exchange anda provider can act upon it.

        This exchange takes the following keys:

         * routingKeyKind: Identifier for the routing-key kind. This is always `'primary'` for the formalized routing key. (required)

         * reserved: Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.
        """

        ref = {
            'exchange': 'worker-pool-created',
            'name': 'workerPoolCreated',
            'routingKey': [
                {
                    'constant': 'primary',
                    'multipleWords': False,
                    'name': 'routingKeyKind',
                },
                {
                    'multipleWords': True,
                    'name': 'reserved',
                },
            ],
            'schema': 'v1/pulse-worker-pool-message.json#',
        }
        return self._makeTopicExchange(ref, *args, **kwargs)

    def workerPoolUpdated(self, *args, **kwargs):
        """
        Worker Pool Updated Messages

        Whenever the api receives a request to update aworker pool, a message is posted to this exchange anda provider can act upon it.

        This exchange takes the following keys:

         * routingKeyKind: Identifier for the routing-key kind. This is always `'primary'` for the formalized routing key. (required)

         * reserved: Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.
        """

        ref = {
            'exchange': 'worker-pool-updated',
            'name': 'workerPoolUpdated',
            'routingKey': [
                {
                    'constant': 'primary',
                    'multipleWords': False,
                    'name': 'routingKeyKind',
                },
                {
                    'multipleWords': True,
                    'name': 'reserved',
                },
            ],
            'schema': 'v1/pulse-worker-pool-message.json#',
        }
        return self._makeTopicExchange(ref, *args, **kwargs)

    def workerPoolDeleted(self, *args, **kwargs):
        """
        Worker Pool Deleted Messages

        Whenever the api receives a request to delete aworker pool, a message is posted to this exchange anda provider can act upon it.

        This exchange takes the following keys:

         * routingKeyKind: Identifier for the routing-key kind. This is always `'primary'` for the formalized routing key. (required)

         * reserved: Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.
        """

        ref = {
            'exchange': 'worker-pool-deleted',
            'name': 'workerPoolDeleted',
            'routingKey': [
                {
                    'constant': 'primary',
                    'multipleWords': False,
                    'name': 'routingKeyKind',
                },
                {
                    'multipleWords': True,
                    'name': 'reserved',
                },
            ],
            'schema': 'v1/pulse-worker-pool-message.json#',
        }
        return self._makeTopicExchange(ref, *args, **kwargs)

    funcinfo = {
    }


__all__ = ['createTemporaryCredentials', 'config', '_defaultConfig', 'createApiClient', 'createSession', 'WorkerManagerEvents']
